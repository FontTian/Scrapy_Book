# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ExamplePipeline(object):
    def process_item(self, item, spider):
        return item

# 实现一个PipLine的组件

class PriceConverterPipeline(object):

    # 英镑对美元汇率
    exchange_rate = 1.412

    def process_item(self,item,spider):
         price = float(item['price'][1:]) * self.exchange_rate

         item['price'] = '$%.2f'%price

         return item

from scrapy.exceptions import DropItem


# 设置过滤器,筛选其他重复样本
class DuplicatesPipeline(object):

    def __init__(self):
        self.book_set = set()

    def process_item(self,item,spider):

        title = item['title']

        if title in self.book_set:
            raise DropItem("Duplicates book found:%s"%item)

        self.book_set.add(title)

        return item

