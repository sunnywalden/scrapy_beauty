import logging

import scrapy

from .proxy import get_proxy
from ..items import BeautyItem

class BeautySpider(scrapy.Spider):
    name = 'siwa'
    allowed_domains = ['huaban.com']
    start_urls = [
        'https://huaban.com/boards/19989494',
    ]

    num = 1
    items_per_page = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger.info('Start generating proxy IP')
        get_proxy()

    def parse(self, response):
        # write the category page data extraction code here

        self.logger.info('Parse function called on %s', response.url)
        if not response.xpath('//div[@class="infinite-scroll-component "]'):
            yield scrapy.Request(url=response.url, dont_filter=True)
        try:
            all_items = response.xpath('//div[@class="infinite-scroll-component "]/div')
        except Exception as e:
            self.logger.error('Error: %s', e.__str__())
            return
        self.logger.info('Got all items:%s', all_items)
        picture_ids, picture_titles, image_urls  = [], [], []
        for pic_item in all_items:
            pic_ids = pic_item.xpath('div/div/@data-pin-id').extract()
            titles = pic_item.xpath('div/div/div/div/a/img/@title').extract()
            img_urls = pic_item.xpath('div/div/div/div/a/img/@src').extract()
            if pic_ids is None or img_urls is None or titles is None or len(pic_ids) == 0 or len(img_urls) == 0 or len(titles) == 0:
                break
            picture_ids.extend(pic_ids)
            picture_titles.extend(titles)
            image_urls.extend(img_urls)
            self.logger.info('%s %s %s', pic_ids, titles, img_urls)
            # break
            # image_path = img_path.split('_')[0]

        total = len(picture_ids)
        for i in range(total):
            image_url = image_urls[i].split('_')[0]
            image_full_path = f'https://huaban.com/pins/{picture_ids[i]}?modalImg={image_url}'
            # image_urls.append(image_full_path)
            image_item = BeautyItem()
            image_item['file_urls'] = [image_full_path]
            yield scrapy.Request(image_full_path, callback=self.parse_beauty, meta={'item': image_item})
        self.logger.info('DEBUG callback "parse": got response %s', response)
        self.logger.info('we have done with this page %s', response.url)


    def parse_beauty(self, response):
        self.logger.info('Get picture from %s', response.url)

        if response.status == 200:
            main = response.xpath('//div[@id="pin_detail"]/div')[0]
            details = main.xpath('div/div/div/div/img')
            image_info = details[0]
            self.logger.info("########### DEBUG details:%s", image_info.extract())
            pic_id= image_info.xpath('@data-content-id').extract_first()
            title = image_info.xpath('@alt').extract_first()
            image_url = image_info.xpath('@src').extract_first()
            if not pic_id or not title or not image_url:
                self.logger.error('Missing data for item: %s', response.url)
                return
            self.logger.info('%s %s', title, image_url)

            beauty = BeautyItem()
            beauty['id'] = pic_id
            beauty['title'] = title
            beauty['file_urls'] = [image_url]
            self.logger.info('Picture resolved:%s %s', title.encode(encoding='utf-8'), image_url)
            yield beauty
            self.logger.info('callback "parse": got response %r' % response)

        else:
            self.logger.info('request url %s returned error', response.url)
            self.logger.debug('callback "parse": got response %r', response)
