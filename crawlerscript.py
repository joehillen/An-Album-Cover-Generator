#!/usr/bin/python

"""
* Copyright (C) 2011 Joe Hillenbrand <joehillen@gmail.com>
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Affero General Public License as
* published by the Free Software Foundation, either version 3 of the
* License, or (at your option) any later version.
* 
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU Affero General Public License for more details.
* 
* You should have received a copy of the GNU Affero General Public License
* along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'albumgen.settings') #Must be at the top before other imports

from scrapy import log, signals, project
from scrapy.xlib.pydispatch import dispatcher
from scrapy.conf import settings
from scrapy.crawler import CrawlerProcess
from multiprocessing import Process, Queue

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

    def _crawl(self, queue, spider_name):
        spider = self.crawler.spiders.create(spider_name)
        if spider:
            self.crawler.queue.append_spider(spider)
    	self.crawler.start()
        self.crawler.stop()
        queue.put(self.items)
    
    def crawl(self, spider):
		queue = Queue()
		p = Process(target=self._crawl, args=(queue, spider,))
		p.start()
		p.join()
		return queue.get(True)

# Usage
if __name__ == "__main__":
	log.start()

	items = list()
	crawler = CrawlerScript()
	for i in range(10):
		items.append(crawler.crawl('pic'))
	print items
