#!/usr/bin/python

# Imports
from covercreator import *
import string, sys
from crawlerscript import *

crawler = CrawlerScript()

# Get Pic
pic_results = crawler.crawl('pic')
pic_item = pic_results[0] if len(pic_results) >= 1 else None
print pic_item

# Get Band Name
band_results = crawler.crawl('band')
band_item = band_results[0] if len(band_results) >= 1 else None
print band_item

# Get Album Name
album_results = crawler.crawl('album')
album_item = album_results[0] if len(album_results) >= 1 else None
print album_item

if pic_item and band_item and album_item:
    create = CoverCreator()
    create.cover('/tmp/albumgen/' + pic_item['pic_path'], band_item['band'], album_item['album'])
else:
    print "Failed to generate album"
