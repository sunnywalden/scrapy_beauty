# -*- coding:utf-8 -*-

import requests


def get_proxy():
    proxies = []
    for i in range(50):
        proxy = 'http://'+requests.get("http://192.168.0.109:5010/get/").json().get('proxy')
        print(proxy)
        proxies.append(proxy)
    with open('/tmp/proxies_beauty.txt', 'a') as f:
        for proxy in proxies:
                f.write(proxy+'\n')

if __name__=='__main__':
    get_proxy()
