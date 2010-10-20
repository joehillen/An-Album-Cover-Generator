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
