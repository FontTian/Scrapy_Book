# -*- coding: utf-8 -*-

import scrapy


class ToscrapeBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

from scrapy import Item,Field

class BookItem(Item):
    title = Field() # 标题,即书名
    price = Field() # 价格
    category = Field() # 分类,类别
    description = Field() # 描述
    star_rating = Field() # 星级
    review_num = Field() # 评价数量
    upc = Field() # 编号
    stock = Field() # 库存
