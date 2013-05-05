from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial.items import NewsItem
from scrapy.http import Request
from scrapy import log
from django.utils.html import escape


class BBCSpider(BaseSpider):
	name = "bbc"
	start_urls = []
	
	def __init__(self, keyword='london'):
	    self.allowed_domains = ["bbc.co.uk"]
	    self.start_urls = [
		'http://www.bbc.co.uk/search/news/?q=%s' % keyword
	    ]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		newsList = hxs.select("//li[contains(@class, 'DateItem')]")
		newsList = newsList.select("ul[contains(@class, 'DateList')]/li[contains(@class, 'linktrack-item')]//a[contains(@class, 'title')]")
		#for news in newsList:
			#title = news.select("text()").extract()
			#link = news.select("@href").extract()
			#log.msg("Link: %s" %link, level=log.INFO)
			#return Request("http://www.bbc.co.uk/news/world-europe-11141340", callback=self.parse_details)
			#return Request(link, callback=self.parse_details)
		return Request("http://www.bbc.co.uk/news/world-europe-11141340", callback=self.parse_details)
	
	def parse_details(self, response):
		hxs = HtmlXPathSelector(response)
		title =  hxs.select("//h1[contains(@class, 'story-header')]/text()").extract()
		content = hxs.select("//div[contains(@class, 'story-body')]").extract()
		link = response.url
		yield NewsItem(title = title[0], content = escape(content[0]), link = link)
		
