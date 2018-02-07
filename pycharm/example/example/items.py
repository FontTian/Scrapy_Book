# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 新添加的BookItem

from scrapy import Item,Field

class BookItem(Item):
    # title = Field(serializer=lambda x:'|'.join(x)) # 处理List 的问题
    # title = Field(serializer=lambda x:str(x)) # 处理List 的问题
    title = Field()
    price = Field()
    category = Field()
    description = Field()