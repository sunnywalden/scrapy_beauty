# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import logging


class ImgDownloadPipeline(ImagesPipeline):

	logger = logging.getLogger(__name__)	
	def get_media_requests(self, item, info):
        	for image_url in item['image_urls']:
			self.logger.info('Start download image %s', image_url)
            		yield Request(image_url,meta={'item':item,'index':item['image_urls'].index(image_url)})


	
	def file_path(self, request, response=None, info=None):
		item = request.meta['item']  # 通过上面的meta传递过来item
		index = request.meta['index']
		beauty_name = item['title'] + '.jpg'
		self.logger.info('the name of beauty that been downloaded right now is %s', beauty_name)
		return beauty_name

