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

