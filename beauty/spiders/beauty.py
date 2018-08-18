from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


import scrapy
from ..items import BeautyItem
import proxy
import logging

#print('start generate proxy ip')
#proxy.get_proxy()
logger = logging.getLogger(__name__)

class BeautySpider(scrapy.Spider):
    
    print('start generate proxy ip')
    proxy.get_proxy()

    name = 'siwa'
    allowed_domains = ['www.27270.com']
    start_urls = [
	'http://www.27270.com/tag/384.html',
	'http://www.27270.com/tag/513.html',
    	'http://www.27270.com/tag/782.html',
	'http://www.27270.com/tag/35.html',
	'http://www.27270.com/tag/288.html',
	'http://www.27270.com/tag/441.html',
	]

    num = 1
    items_per_page = 0

    def parse(self, response):
		items = []
        # write the category page data extraction code here

		logger.info('Parse function called on %s', response.url)
		if not response.xpath('//ul[@id="Tag_list"]'):
    			yield Request(url=response.url, dont_filter=True)

		for li in response.xpath('//ul[@id="Tag_list"]'):
			titles = li.xpath('li/a/@title').extract()
			imgs = li.xpath('li/a/img/@src').extract()
			pages = li.xpath('li/a/@href').extract()
			
			logger.info('%s %s %s',titles,imgs,pages)
		total = len(titles)

		for i in range(total):
			self.logger.info('%s %s',titles[i],pages[i])
			yield scrapy.Request(pages[i],callback=self.parse_beauty)
		self.logger.debug('callback "parse": got response %s',response)
		logger.info('we have done with this page %s',response.url)

		while total <= total:   #There is 30 items per page
			next_page = response.xpathfo('//div[@class="TagPage"]/ul/li/a/@href').extract()[-2]
			url = 'http://www.27270.com' + next_page
			self.logger.info('Crawl for next page now %s',url)
			yield scrapy.Request(url, callback=self.parse)


    def parse_beauty(self, response):

	if not response.xpath('//div[@id="picBody"]'):
		yield Request(url=response.url, dont_filter=True)
	
	if response.status==200:	
		detail = response.xpath('//div[@id="picBody"]')
		title = detail.xpath('p/a/img/@alt').extract()[0]
		image_url = detail.xpath('p/a/img/@src').extract()[0]
		self.logger.info( '%s %s',title,image_url)

		beauty = BeautyItem()	
#		beauty['title'] = title
		beauty['image_urls'] = [image_url]

#		yield beauty
#		self.logger.debug('callback "parse": got response %r' % response)

		pages = response.xpath('//ul[@class="articleV4Page l"]')
		total_pages = pages.xpath('li[@class="hide"]/@pageinfo').extract()[0]
		current_page = pages.xpath('li[@class="thisclass"]/a[@href="#"]/text()').extract()[0]
		next_page = pages.xpath('li[@id="nl"]/a/@href').extract()[0]
		beauty['title'] = title + current_page
		self.logger.info('Starting crawl for next page of %s',beauty['title'])	
		
		yield beauty
		self.logger.debug('callback "parse": got response %r' % response)
		
		url = response.url
		next_page_url = '/'.join(url.split('/')[0:-1]) + '/' + next_page
		self.logger.info('There are %s pages out there.scrath for next page %s', total_pages,next_page_url)
		yield scrapy.Request(next_page_url, callback=self.parse_beauty)
	else:
		self.logger.info('request url %s returned error',request.url)
		self.logger.debug('callback "parse": got response %r' % response)
