# -*- coding: utf-8 -*-
import scrapy
from ..items import BookItem
from scrapy.linkextractors import LinkExtractor

class BooksSpider(scrapy.Spider):

    name = 'books'
    start_urls = ['http://books.toscrape.com/', ]


    def parse(self, response):
        for book_url in response.css("article.product_pod > h3 > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)
        # 提取下一页的链接
        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)

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
        bookitem['star_rating'] = response.css('div.product_main p.star-rating::attr(class)').re_first('star-rating ([A-Za-z]+)')

        # 注意此处的性能问题,先创建CSS的selector对象再解析xpath的速度要远慢于额外创建一个selector对象
        table = response.css('table.table.table-striped')
        bookitem['upc'] = table.xpath('(.//tr)[1]/td/text()').extract_first()
        bookitem['stock'] = table.xpath('(.//tr)[last()-1]/td/text()').re_first('\((\d+) available\)')
        bookitem['review_num'] = table.xpath('(.//tr)[last()]/td/text()').extract_first()

        yield bookitem
