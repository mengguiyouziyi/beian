# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql


class MysqlPipeline(object):
	"""
	本机 localhost；公司 etl2.innotree.org；服务器 etl1.innotree.org
	"""

	def __init__(self):
		self.conn = pymysql.connect(host='etl1.innotree.org', port=3308, user='spider', password='spider', db='spider',
		                            charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		# self.conn = pymysql.connect(host='localhost', user='root', password='3646287', db='spider', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		# sql = """insert into kuchuan_all(id, app_package, down, trend) VALUES(%s, %s, %s, %s) ON DUPLICATE KEY UPDATE app_package=VALUES(app_package), down=VALUES(down), down=VALUES(trend)"""
		sql = """replace into beian (search_id, search_domain, detai_url, is_allow, base_lice_key, check_time, com_name, com_nature, site_name, home_url, principal, domains, lice_key, exam_item, crawl_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
		args = (item["search_id"], item["search_domain"], item["detai_url"], item["is_allow"], item["base_lice_key"],
		        item["check_time"], item["com_name"], item["com_nature"], item["site_name"], item["home_url"],
		        item["principal"], item["domains"], item["lice_key"], item["exam_item"], item["crawl_time"])
		self.cursor.execute(sql, args=args)
		self.conn.commit()

		print(str(item['lice_key']) + ' success')
