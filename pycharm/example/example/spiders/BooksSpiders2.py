#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:fonttian 
@file: BookSpider.py
@time: 2018/01/31
"""
import scrapy
from ..items import BookItem

class BooksSpider(scrapy.Spider):

    # name 每个爬虫的唯一标识
    name = "books2"

    start_urls = ['http://books.toscrape.com/',]

    def parse(self, response):
        for book_url in response.css("article.product_pod > h3 > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)
        # 提取下一页的链接
        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
            
    def parse_book_page(self, response):
        bookitem = BookItem()
        product = response.css("div.product_main")
        bookitem["title"] = product.css("h1 ::text").extract_first()
        bookitem['category'] = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()"
        ).extract_first()
        bookitem['description'] = response.xpath(
            "//div[@id='product_description']/following-sibling::p/text()"
        ).extract_first()
        bookitem['price'] = response.css('p.price_color ::text').extract_first()
        yield bookitem


