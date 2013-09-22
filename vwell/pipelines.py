# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class VwellPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):

	def __init__(self):
		self.file = open('medicalList.json', 'w')

	def process_item(self, item, spider):
		newItem = {}
		newItem['name'] = item['name'].encode('utf-8')
		newItem['phone'] = item['phone'].encode('utf-8')
		newItem['address'] = item['address'].encode('utf-8')

		line =  '{ "name" : "%s", "phone" : "%s", "address" : "%s" },' %(newItem['name'], newItem['phone'], newItem['address']) + '\n'
		self.file.write(line)
		return item

class JsonWriter2Pipeline(object):

	def __init__(self):
		self.file = open('healthList.json', 'w')

	def process_item(self, item, spider):
		newItem = {}
		newItem['name'] = item['name'].encode('utf-8')
		newItem['phone'] = item['phone']
		newItem['address'] = item['address'].encode('utf-8')
		newItem['home_page'] = item['home_page'].encode('utf-8')

		line =  '{ "name" : "%s", "phone" : ["%s", "%s"], "address" : "%s", "home_page" : "%s" },' %(newItem['name'], newItem['phone'][0].encode('utf-8'), newItem['phone'][1].encode('utf-8'), newItem['address'], newItem['home_page']) + '\n'
		self.file.write(line)
		return item