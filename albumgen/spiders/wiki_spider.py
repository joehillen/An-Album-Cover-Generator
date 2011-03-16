
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

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from albumgen.items import AlbumgenItem

class WikiSpider(BaseSpider):
	name = "band"
	start_urls = ["http://en.wikipedia.org/wiki/Special:Random"]

	def parse (self, response):
		hxs = HtmlXPathSelector(response)
		item = AlbumgenItem()
		item['identifier'] = "band"
		item['band'] = hxs.select('//title/text()').re('^[^-\(,]+')[0].strip()
		return item

SPIDER = WikiSpider()

