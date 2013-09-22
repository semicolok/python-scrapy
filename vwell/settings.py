# Scrapy settings for vwell project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'vwell'

SPIDER_MODULES = ['vwell.spiders']
NEWSPIDER_MODULE = 'vwell.spiders'
ITEM_PIPELINES = [
	# 'vwell.pipelines.JsonWriterPipeline'
	'vwell.pipelines.JsonWriter2Pipeline'
]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'vwell (+http://www.yourdomain.com)'
