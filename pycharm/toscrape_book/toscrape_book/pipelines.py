# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ToscrapeBookPipeline(object):
    def process_item(self, item, spider):
        return item


class StarRatingPipeline(object):

    star_rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,

    }

    def process_item(self,item,spider):
        rating = item.get('star_rating')
        if rating:
            item['star_rating'] = self.star_rating_map[rating]

        return item

# use mongodb

from pymongo import MongoClient
from scrapy import Item


class MongoDBPipline:

    def open_spider(self, spider):
        db_url = spider.settings.get('MONGODBURL', 'mongodb://localhost:27017')
        db_name = spider.settings.get('MONGODB_DB_NAME', 'scrapy_default')

        self.db_client = MongoClient('mongodb://localhost:27017')
        self.db = self.db_client[db_name]

    def close_spider(self, spider):
        self.db_client.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        if isinstance(item, Item):
            item = dict(item)

        self.db.books.insert_onr(item)