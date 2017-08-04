import re

sites = set()
with open('/Users/menggui/Desktop/result_4g_sichuan_20170208.txt', 'r') as f:
	with open('/Users/menggui/Desktop/result_4g_sichuan_20170208_handled.txt', 'a') as f1:
		for url in f.readlines():
			print(url)
			site = re.search(r'([-\w]+\.(com|cn|com\.cn|net|org|gov|edu|int|mil|biz|info|tv|pro|name|museum|coop|aero|CC|SH|ME|asia|kim|hk))', url)
			num = re.search(r'\s+(\d+)', url)
			if site and num:
				num = int(num.group(1).strip())
				if num >= 5:
					site = site.group(1).strip()
					if site not in sites:
						print(site)
						f1.write(site+'\n')
						sites.add(site)




