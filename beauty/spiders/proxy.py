# -*- coding:utf-8 -*-

import requests


def get_proxy():
	proxie = []
	for i in range(50):
		proxy = 'http://'+requests.get("http://123.207.35.36:5010/get/").content
		print(proxy)
		proxie.append(proxy)
	with open('/tmp/proxies_beauty.txt', 'a') as f:
		for proxy in proxie:
        		f.write(proxy+'\n')

if __name__=='__main__':
	get_proxy()
