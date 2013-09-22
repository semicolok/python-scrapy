# -*- coding:utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from vwell.items import MedicalItem

class VwellSpider(BaseSpider):
	name = 'vwell'
	allowed_domains = ['cdc.go.kr']
	start_urls = ['https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100000&CURPAGE=1&SelFlag=RPM']

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		medicals = hxs.select('//*[@id="searchFrm"]/fieldset/table/tbody/tr')
		items = []
		count = 0

		for medical in medicals:
			item = MedicalItem()
			item['name'] = medical.select('//td')[count*4].select('a/text()').extract()[0]
			item['phone'] = medical.select('//td')[count*4+1].select('text()').extract()[0]
			item['address'] = medical.select('//td')[count*4+2].select('text()').extract()[0]
			count += 1
			items.append(item)

		return items