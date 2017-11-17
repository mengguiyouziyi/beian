# -*- coding: utf-8 -*-
import re
import scrapy
import time
from urllib.parse import urljoin, quote
from beian.items import BeianItem
from beian.utility.info import rc
from scrapy.exceptions import CloseSpider


class BeianInfoSpider(scrapy.Spider):
	name = 'comp_name'

	def start_requests(self):
		# x = 0
		# while True:
		# 	beian_id_name = rc.rpop('beian_id_name')
		# 	if not beian_id_name:
		# 		x += 1
		# 		if x > 3:
		# 			raise CloseSpider('no datas')
		# 		time.sleep(60)
		# 		continue
			beian_id_name = '10022956169995483090~常州众股网络科技有限公司'
			id_name = beian_id_name.split('~')
			print(id_name)
			item = BeianItem()
			item['comp_id'] = id_name[0]
			item['comp_full_name'] = id_name[1]
			url = 'http://www.beianbeian.com/s?keytype=2&q=%s' % item['comp_full_name']
			yield scrapy.Request(url, meta={'item': item})


def parse(self, response):
	if '没有符合条件的记录，即未备案' in response.text:
		return
	item = response.meta.get('item', '')
	if not item:
		return
	lice_key_obj = response.xpath(".//*[@id='show_table']/tr[2]/td[4]/a[1]/text()").extract_first()
	lice_key = lice_key_obj.strip() if lice_key_obj else ''
	base_lice_key = re.search(r'(.+)(\-\d{1,4})', lice_key).group(1) if lice_key else ''
	rever_url = 'http://www.beianbeian.com/search-1/%s' % quote(base_lice_key) if base_lice_key else ''
	if rever_url:
		yield scrapy.Request(rever_url, callback=self.parse_rever, meta={'item': item})


def parse_rever(self, response):
	item = response.meta.get('item', '')
	if not item:
		return
	trs_obj = response.xpath(".//*[@id='show_table']/tr")
	for tr_obj in trs_obj:
		detai_url = tr_obj.xpath("./td[9]/a/@href").extract_first()
		if not detai_url:
			continue
		detai_url = urljoin(response.url, detai_url)
		is_allow = tr_obj.xpath("./td[8]/span/text()").extract_first()
		item['detai_url'] = detai_url
		item['is_allow'] = is_allow if is_allow else ''
		yield scrapy.Request(detai_url, callback=self.parse_detail, meta={'item': item})


def parse_detail(self, response):
	item = response.meta.get('item', '')
	if not item:
		return
	table1 = response.xpath('//table[1]')
	table2 = response.xpath('//table[2]')

	base_lice_key = table1.xpath('./tr[2]/td[2]/text()').extract_first()
	check_time = table1.xpath('./tr[2]/td[4]/text()').extract_first()
	com_name = table1.xpath('./tr[3]/td[2]/text()').extract_first()
	com_nature = table1.xpath('./tr[3]/td[4]/text()').extract_first()

	site_name = table2.xpath('./tr[2]/td[2]/text()').extract_first()
	home_url = table2.xpath('./tr[2]/td[4]//a/text()').extract()
	principal = table2.xpath('./tr[3]/td[2]/text()').extract_first()
	domain = table2.xpath('./tr[3]/td[4]//a/text()').extract()
	lice_key = table2.xpath('./tr[4]/td[2]/a/text()').extract_first()
	exam_item_obj = table2.xpath('./tr[4]/td[4]/text()').extract()
	exam_item = [exam.strip() for exam in exam_item_obj if exam.strip()] if exam_item_obj else ''

	item['base_lice_key'] = base_lice_key if base_lice_key else ''
	item['check_time'] = check_time if check_time else ''
	item['com_name'] = com_name if com_name else ''
	item['com_nature'] = com_nature if com_nature else ''
	item['site_name'] = site_name if site_name else ''

	item['home_url'] = str(home_url) if home_url else ''
	item['principal'] = principal if principal else ''

	item['domains'] = str(domain) if domain else ''
	item['lice_key'] = lice_key if lice_key else ''

	item['exam_item'] = str(exam_item) if exam_item else ''

	yield item
