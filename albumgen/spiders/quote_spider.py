from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from albumgen.items import AlbumgenItem
import re

class QuoteSpider(BaseSpider):
	name = "album"
	start_urls = ["http://www.quotationspage.com/random.php3"]
	
	def parse (self, response):
		hxs = HtmlXPathSelector(response)
		item = AlbumgenItem()
		quote = hxs.select('//dt[@class="quote"]/a/text()')[9].extract()
		regex = re.compile('([\w\']+\s+){3}[\w+\']+\.$')
		match = regex.search(quote)
		item['identifier'] = "album"
		item['album'] = match.group().rstrip('.')
		return item

SPIDER = QuoteSpider()

