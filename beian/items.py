# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeianItem(scrapy.Item):
	# 搜索域名 的序号
	comp_id = scrapy.Field()
	comp_full_name = scrapy.Field()
	# 搜索域名
	search_domain = scrapy.Field()

	# 域名备案详情信息页
	detai_url = scrapy.Field()
	# 是否限制接入
	is_allow = scrapy.Field()

	# 备案/许可证号
	base_lice_key = scrapy.Field()
	# 审核通过时间
	check_time = scrapy.Field()
	# 主办单位名称
	com_name = scrapy.Field()
	# 主办单位性质
	com_nature = scrapy.Field()

	# 网站名称
	site_name = scrapy.Field()
	# 网站首页网址
	home_url = scrapy.Field()
	# 网站负责人姓名
	principal = scrapy.Field()
	# 网站域名
	domains = scrapy.Field()
	# 网站备案/许可证号
	lice_key = scrapy.Field()
	# 网站前置审批项
	exam_item = scrapy.Field()
