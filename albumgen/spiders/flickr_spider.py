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

