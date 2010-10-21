#!/usr/bin/python
import os
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'albumgen.settings') #Must be at the top before other imports

from scrapy import log, signals, project
from scrapy.xlib.pydispatch import dispatcher
from scrapy.conf import settings
from scrapy.crawler import CrawlerProcess

class CrawlerScript():

    def __init__(self):
		self.crawler = CrawlerProcess(settings)
		if not hasattr(project, 'crawler'):
			self.crawler.install()
		self.crawler.configure()
		self.items = []
		dispatcher.connect(self._item_passed, signals.item_passed)

    def _item_passed(self, item):
        self.items.append(item)

    def start(self):
    	self.crawler.start()
    
    def stop(self):
    	self.crawler.stop()

    def addSpider(self, spider_name):
        spider = self.crawler.spiders.create(spider_name)
        if spider:
            self.crawler.queue.append_spider(spider)
            
# Usage
if __name__ == "__main__":
	log.start()

	c = CrawlerScript()
	c.addSpider('pic')
	c.addSpider('album')
	c.start()
	print c.items
	c.stop()
