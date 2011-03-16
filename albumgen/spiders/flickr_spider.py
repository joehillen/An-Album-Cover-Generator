
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

class FlickrSpider(BaseSpider):
	name = "pic"
	start_urls = ["http://www.flickr.com/explore/interesting/7days"]

	def parse (self, response):
		hxs = HtmlXPathSelector(response)
		item = AlbumgenItem()
		item['identifier'] = "pic"
		item['pic'] = hxs.select("//td[@class='Photo'][2]/span/a/img/@src")[2].extract().replace('_m.jpg','.jpg')
		return item

SPIDER = FlickrSpider()

