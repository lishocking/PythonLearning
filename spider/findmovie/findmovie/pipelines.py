# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import csv


class FindmoviePipeline(object):
#    def __init__(self):
#        self.file = open('items.jl', 'w')
#
    def process_item(self, item, spider):
#        line = json.dumps(dict(item)) + "\n"
#        self.file.write(line)
        return item

class SaveMovieInfoPipeline(object):
        def __init__(self):
            self.file = open ('test.csv','w')
#            self.cx=sqlite3.connect("/test.db")
#            self.cu=self.cx.cursor()
#            self.cu.execute("create table movies(name text,des text)"
        def process_item(self,item,spider):
            csvfile = csv.writer(self.file, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvfile.writerow(item.items())
            return item
import pymongo

class MongoPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item

