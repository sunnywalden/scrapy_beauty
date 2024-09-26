# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

import pymysql
from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings  # 导入settings配置

from .items import BeautyItem

logger = logging.getLogger(__name__)


class FileDownloadPipeline(FilesPipeline):
    logger = logging.getLogger(__name__)

    def get_media_requests(self, item, info):
        self.logger.info('FileDownloadPipeline: Processing item %s', item)
        adapter = ItemAdapter(item)
        for image_url in adapter['file_urls']:
            # image_id = image_url.split('/')[-1]
            # beauty_name = image_id + ".jpg"
            self.logger.info('Start download image %s', image_url)
            yield Request(image_url)

    def file_path(self, request, response=None, info=None, *, item=None):
        beauty_name = request.url.split('/')[-1] + '.jpg'

        self.logger.info(f'the name of beauty that been downloaded right now is %s', beauty_name)
        return beauty_name

class BeautyItemPipeline(object):
    """保存到数据库中对应的class
       1、在settings.py文件中配置
       2、在自己实现的爬虫类中yield item,会自动执行"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def db_handle():
        '''1、@classmethod声明一个类方法，而对于平常我们见到的叫做实例方法。
               2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
               3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
        # 读取settings中配置的数据库参数
        settings = get_project_settings()
        conn = pymysql.connect(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
        )
        if conn:
            logger.info('Connect to mysql success!')
        return conn

    # pipeline默认调用
    def process_item(self, item, spider):
        # 写入数据库中
        # SQL语句在这里
        conn = self.db_handle()
        cursor = conn.cursor()
        if isinstance(item, BeautyItem):
            self.logger.info('Handle beauty %s item now', item['id'])
            sql = "insert ignore into beauty(id,title,image_url) values(%s,%s,%s)"
            params = (item['id'], item['title'], item['file_urls'][0])
            self.logger.info(sql, item['id'], item['title'], item['file_urls'][0])
        else:
            self.logger.error('Not a beauty item: %s', item['title'])
        try:
            cursor.execute(sql, params)
            conn.commit()
        # 关闭连接
        except Exception as error:
            # 出现错误时打印错误日志
            self.logger.info(error)
            conn.rollback()
        return item
