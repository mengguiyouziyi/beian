# -*- coding: utf-8 -*-
import re
from urllib.parse import urljoin, quote
import scrapy
from beian.items import BeianItem


class BeianInfoSpider(scrapy.Spider):
	name = 'comp_site'

	def __init__(self):
		with open('beian/result_4g_sichuan_20170208_handled.txt', 'r') as f:
			self.search_domains = f.readlines()

	def start_requests(self):
		# self.search_domains = ['baidu.com']
		for search_id, search_domain in enumerate(self.search_domains):
			item = BeianItem()
			item['search_id'] = search_id
			item['search_domain'] = search_domain.strip()
			url = 'http://www.beianbeian.com/search/%s' % search_domain
			yield scrapy.Request(url, meta={'item': item}, dont_filter=True)

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
			yield scrapy.Request(rever_url, callback=self.parse_rever, meta={'item': item}, dont_filter=True)

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
			yield scrapy.Request(detai_url, callback=self.parse_detail, meta={'item': item}, dont_filter=True)

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









		# com_obj = response.xpath('//div[@id="kind"]/text()').extract()
		# com_name = com_obj[0] if len(com_obj) >= 1 else ''
		# nature = com_obj[1] if len(com_obj) > 1 else ''
		# lice_key_obj = response.xpath(".//*[@id='show_table']/tr[2]/td[4]/a[1]/text()").extract_first()
		# lice_key = lice_key_obj.strip() if lice_key_obj else ''
		#
		# base_lice_key = re.search(r'(.+)(\-\d{1,4})', lice_key).group(1) if lice_key else ''
		#
		# detai_url = response.xpath(".//*[@id='show_table']/tr[2]/td[4]/a[1]/@href").extract_first()
		#
		# rever_url = 'http://www.beianbeian.com/search-1/%s' % quote(base_lice_key) if base_lice_key else ''
		#
		# site_name_obj = response.xpath(".//*[@id='show_table']/tr[2]/td[5]/text()").extract_first()
		# site_name = site_name_obj.strip() if site_name_obj else ''
		#
		# home_url_obj = response.xpath(".//*[@id='home_url']/div/a/@href").extract()
		# home_url = [re.search(r'url=(.*)', url).group(1) for url in home_url_obj] if home_url_obj else []
		#
		# check_time_obj = response.xpath(".//*[@id='pass_time']/text()").extract_first()
		# check_time = check_time_obj.strip() if check_time_obj else ''
		#
		# principal_obj = response.xpath('html/body/div[1]/table[2]/tbody/tr[3]/td[2]/text()').extract_first()
		# principal = principal_obj.strip() if principal_obj else ''
		# site_url = response.xpath("html/body/div[1]/table[2]/tbody/tr[3]/td[4]/div/div/a//text()").extract()
		# exam_item = response.xpath("html/body/div[1]/table[2]/tbody/tr[4]/td[4]//text()").extract()










