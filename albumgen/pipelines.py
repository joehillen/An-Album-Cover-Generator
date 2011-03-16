
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

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request

class PicPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['identifier'] == 'pic':
            return Request(item['pic'])

    def item_completed(self, results, item, info):
    	for success, info in results:
    		if success and item['identifier'] == 'pic':
    			item['pic_path'] = info['path']
        return item

