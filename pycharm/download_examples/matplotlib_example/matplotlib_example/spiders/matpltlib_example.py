# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import DownloadMatplotlibFilesItem

class MatpltlibExampleSpider(scrapy.Spider):
    name = 'matpltlib_example'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound li.toctree-l2',deny='/index.html')

        print(len(le.extract_links(response)))

        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_downloadfiles)

    def parse_downloadfiles(self,response):
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        downloadfiles = DownloadMatplotlibFilesItem()
        downloadfiles['file_urls'] = [url]
        return downloadfiles