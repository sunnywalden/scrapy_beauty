# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
#from scrapy import log


#class BeautyPipeline(object):
#    def process_item(self, item, spider):
#        
#	return item

class ImgDownloadPipeline(ImagesPipeline):
	
	def get_media_requests(self, item, info):
        	for image_url in item['image_urls']:
			print('Start download image', image_url)
            		yield Request(image_url,meta={'item':item,'index':item['image_urls'].index(image_url)})


	
	def file_path(self, request, response=None, info=None):
		item = request.meta['item']  # 通过上面的meta传递过来item
		index = request.meta['index']
		beauty_name = item['title'] + '.jpg'
		print('beauty name is', beauty_name)
		return beauty_name

#    	def item_completed(self, results, item, info):
#        	image_paths = [x['path'] for ok, x in results if ok]
#        	if not image_paths:
#            		raise DropItem("Item contains no images")
#        	item['image_paths'] = image_paths
#        	return item
