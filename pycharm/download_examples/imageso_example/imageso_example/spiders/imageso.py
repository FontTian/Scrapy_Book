# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from ..items import ImagesoExampleItem

class ImagesoSpider(scrapy.Spider):
    name = 'imageso'

    MAX_DOWNLOAD_NUM = 1000
    BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'

    start_index= 0
    start_urls = [BASE_URL % 0]

    def parse(self, response):

        infos = json.loads(response.body.decode('utf-8'))
        yield {'image_urls':[info['qhimg_url'] for info in infos['list']]}


        self.start_index += infos['count']

        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield Request(self.BASE_URL%self.start_index)

