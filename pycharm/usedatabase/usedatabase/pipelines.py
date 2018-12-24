# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class UsedatabasePipeline(object):
    def process_item(self, item, spider):
        return item


from pymongo import MongoClient
from scrapy import Item

class MongoDBPipline(object):

    def open_spider(self,spider):
        db_url = spider.settings.get('MONGODBURL','mongodb://localhost:27017')
        db_name = spider.settings.get('MONGODB_DB_NAME','scrapy_default')

        self.db_client = MongoClient(db_url)
        self.db = self.db_client[db_name]

    def close_spider(self,spider):
        self.db_client.close()

    def process_item(self,item,spider):
        self.insert_db(item)
        return item

    def insert_db(self,item):
        if isinstance(item,Item):
            item = dict(item)

        self.db.books.insert_onr(item)


# 使用硬编码
from scrapy.conf import settings
class MongoDBPipline2(object):


    def open_spider(self,spider):

        self.db_client = MongoClient(settings["MONGODB_URL"])
        self.db = self.db_client[settings["scrapy_toscrape_book"]]

    def close_spider(self,spider):
        self.db_client.close()

    def process_item(self,item,spider):
        self.insert_db(item)
        return item

    def insert_db(self,item):
        if isinstance(item,Item):
            item = dict(item)

        self.db.books.insert_onr(item)



