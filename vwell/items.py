# -*- coding:utf-8 -*-

from scrapy.item import Item, Field

class MedicalItem(Item):
	name = Field()
	phone = Field()
	address = Field()

class HealthItem(Item):
	name = Field()
	phone = Field()
	address = Field()
	home_page = Field()
