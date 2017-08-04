# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeianItem(scrapy.Item):
	search_id = scrapy.Field()
	search_domain = scrapy.Field()

	is_allow = scrapy.Field()

	com_name = scrapy.Field()
	com_nature = scrapy.Field()
	lice_key = scrapy.Field()
	base_lice_key = scrapy.Field()
	detai_url = scrapy.Field()
	# rever_url = scrapy.Field()
	site_name = scrapy.Field()
	home_url = scrapy.Field()
	check_time = scrapy.Field()
	domains = scrapy.Field()
	principal = scrapy.Field()
	exam_item = scrapy.Field()

	crawl_time = scrapy.Field()
