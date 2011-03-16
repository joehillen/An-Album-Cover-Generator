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
