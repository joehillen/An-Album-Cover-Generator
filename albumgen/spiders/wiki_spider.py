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

