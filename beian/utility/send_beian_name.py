# coding:utf-8

import os
import sys
import time
from os.path import dirname

father_path = dirname(dirname(os.path.abspath(dirname(__file__))))
base_path = dirname(dirname(os.path.abspath(dirname(__file__))))
path = dirname(os.path.abspath(dirname(__file__)))
sys.path.append(path)
sys.path.append(base_path)
sys.path.append(father_path)

from app.utils.info import rc, kaifa


def selectFun(start):
	cursor = kaifa.cursor()
	sql = """select comp_id, comp_full_name from comp_base_info limit {start}, 500000""".format(start=start)
	cursor.execute(sql)
	results = cursor.fetchall()
	return results


def send_key(key):
	start = i = 0
	while True:
		results = selectFun(start)
		if not results:
			return
		start += len(results)
		values = [result['comp_id'] + '~' + result['comp_full_name'] for result in results]
		for value in values:
			i += 1
			rc.lpush(key, value)
			print(i)


if __name__ == '__main__':
	send_key(key='beian_id_name')
