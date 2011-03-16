
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

# Scrapy settings for albumgen project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

BOT_NAME = 'albumgen'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['albumgen.spiders']
NEWSPIDER_MODULE = 'albumgen.spiders'
DEFAULT_ITEM_CLASS = 'albumgen.items.AlbumgenItem'
ITEM_PIPELINES = ['albumgen.pipelines.PicPipeline']
IMAGES_STORE = '/tmp/albumgen/'
IMAGES_EXPIRE = 1
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

LOG_ENABLED = True # avoid log noise
