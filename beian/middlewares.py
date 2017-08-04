# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64
from random import choice

# 代理服务器
proxyServer = "http://proxy.abuyun.com:9020"

# 代理隧道验证信息
# proxyUser = "H4XGPM790E93518D"
# proxyPass = "2835A47D56143D62"

# 1
# proxyUser = "HQ78N3Y82239165D"
# proxyPass = "AA99073C3271DBFA"

# 2
# proxyUser = "HP098K11Z863G14D"
# proxyPass = "2EBC19D19C17D8ED"

# 3
# proxyUser = "H9SE505130760R6D"
# proxyPass = "FBBA776C3C72866D"

# 4
# proxyUser = "H9CF0585O0838O5D"
# proxyPass = "3E1CA8BB33560FF6"

# 5
# proxyUser = "H8K84WW7038741GD"
# proxyPass = "67EC4B76C72A235C"

# 百科的账号
# 1
proxyUser = "HFHLW2A7NGN6X47D"
proxyPass = "49A144B806CFD145"

# 2
# proxyUser = "H20X28E37Z5R11UD"
# proxyPass = "61CE0860F50555CB"

# 3
# proxyUser = "H51N0CWJLZX5981D"
# proxyPass = "24606F3C6193A99D"

# 4
# proxyUser = "HL6O95146U41Z61D"
# proxyPass = "8F2622D2D6A1A73F"

# 5
# proxyUser = "HI4Z5PI5D1Y44S2D"
# proxyPass = "5D698C9C15113ACE"

# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):
	def process_request(self, request, spider):
		request.meta["proxy"] = proxyServer
		request.headers["Proxy-Authorization"] = proxyAuth


class RetryMiddleware(object):
	def process_response(self, request, response, spider):
		if response.status == 429:
			# print('wrong status: %s, retrying~~' % response.status, request.meta['item']['app_package'])
			return request.replace(url=request.url)
		else:
			return response

	def process_exception(self, request, exception, spider):
		return request.replace(url=request.url)


class RotateUserAgentMiddleware(object):
	"""Middleware used for rotating user-agent for each request"""

	def __init__(self, agents):
		self.agents = agents

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings.get('USER_AGENT_CHOICES', []))

	def process_request(self, request, spider):

		request.headers.setdefault('User-Agent', choice(self.agents))
