# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from beian.utility.info import etl


class MysqlPipeline(object):
	def __init__(self):
		self.conn = etl
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		sql = """insert into beian_over_name (comp_id, comp_full_name, search_domain, detai_url, is_allow, base_lice_key, check_time, com_name, com_nature, site_name, home_url, principal, domains, lice_key, exam_item) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
		args = (item["comp_id"], item["comp_full_name"], item["search_domain"], item["detai_url"], item["is_allow"],
		        item["base_lice_key"],
		        item["check_time"], item["com_name"], item["com_nature"], item["site_name"], item["home_url"],
		        item["principal"], item["domains"], item["lice_key"], item["exam_item"])
		self.cursor.execute(sql, args=args)
		self.conn.commit()

		print(item['comp_full_name'] + ' success')
