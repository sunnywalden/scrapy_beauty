from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


import scrapy
from ..items import BeautyItem

#class BeautySpider(CrawlSpider):
class BeautySpider(scrapy.Spider):
    name = 'siwa'
    allowed_domains = ['www.27270.com']
    start_urls = ['http://www.27270.com/tag/513.html']
    image_urls = []

#    def parse_category(self, response):
    def parse(self, response):
        # write the category page data extraction code here

		for li in response.xpath('//ul[@id="Tag_list"]'):
			print(li)
			titles = li.xpath('li/a/@title').extract()
			sources = li.xpath('li/a/img/@src').extract()
			print(titles,sources)
		image_urls = sources
		total = len(sources)
		print(total)

		for i in range(total):
			item = BeautyItem()
			item['title'] = titles[i]
			item['image_urls'] = [sources[i]]
			print(item)
			yield item
		self.logger.debug('callback "parse": got response %r' % response)
