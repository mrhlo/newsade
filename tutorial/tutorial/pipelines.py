# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo import MongoClient
from scrapy import log


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
        
        
class DBWriterPipeline(object):
	def process_item(self, item, spider):
		mongo = MongoClient()
		newsDB = mongo['newsDB']
		newsItem = dict(item)
		log.msg("Item is %s" %newsItem['content'], log.INFO)
		newsDB.news.insert(newsItem)
		return item
		
	
