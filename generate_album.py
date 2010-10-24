#!/usr/bin/python

# Imports
from covercreator import *
import string, sys
from crawlerscript import *

crawler = CrawlerScript()
pic_item = crawler.crawl('pic')[0]
print pic_item
band_item = crawler.crawl('band')[0]
print band_item
album_item = crawler.crawl('album')[0]
print album_item

create = CoverCreator()
create.cover('/tmp/albumgen/' + pic_item['pic_path'], band_item['band'], album_item['album'])
