from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from vwell.items import HealthItem

class HealthSpider(BaseSpider):
    name = "health"
    allowed_domains = ["cdc.go.kr"]
    start_urls = [
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=1100000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=2600000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=2700000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=2800000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=2900000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=3000000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=3100000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=3600000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=4100000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=4200000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=4300000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=4400000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=4500000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=4600000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=4700000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=4800000000&SelFlag=HC",
    	"https://nip.cdc.go.kr/nip/manage.do?service=getMedicalCenterList&ARTICLECNT=100&CURPAGE=1&SIDCOD=5000000000&SelFlag=HC"
    ]

    def parse(self, response):
		hxs = HtmlXPathSelector(response)
		healths = hxs.select('//*[@id="contents"]/div[@class="conbox sch"]/div[@class="tableA"]/table/tbody/tr')
		items = []
		count = 0

		for health in healths:
			item = HealthItem()
			item['name'] = health.select('//td')[count*4].select('text()').extract()[0]
			item['phone'] = health.select('//td')[count*4+1].select('ul/li')[0].select('text()').extract()
			item['phone'].append(health.select('//td')[count*4+1].select('ul/li')[1].select('text()').extract()[0])
			item['address'] = health.select('//td')[count*4+2].select('text()').extract()[0]
			item['home_page'] = health.select('//td')[count*4+3].select('a/@href').extract()[0]
			count += 1
			items.append(item)

		return items