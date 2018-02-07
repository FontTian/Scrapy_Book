#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:fonttian 
@file: BookSpider.py 
@time: 2018/01/31 
"""
import scrapy

class BooksSpider(scrapy.Spider):

    # name 每个爬虫的唯一标识
    name = "books"

    start_urls = ['http://books.toscrape.com/',]

    def parse(self, response):
        for book in response.css('article.product_pod'):

            title = book.xpath('./h3/a/@title').extract_first()
            price = book.css('p.price_color::text').extract_first()

            yield {
                'title':title,
                'price':price
            }
        # 提取下一页的链接


        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, callback=self.parse)

