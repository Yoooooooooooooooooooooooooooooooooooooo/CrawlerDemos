#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'爬取百度首页实时热点'

__author__ = 'Lyu'

import json
import requests
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
'Host': 'www.baidu.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Upgrade-Insecure-Requests': '1',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Cookie': 'BDUSS=BUR1ZuSEloZ21qUUxDeDZqZDU2fmEtZnpLRHJDeWVRN0VyOGhzUjFjS0NxdFphQUFBQUFBJCQAAAAAAAAAAAEAAACEOzoEX8unX18AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIdr1qCHa9acH'}

try:
    r = requests.get('https://www.baidu.com/home/pcweb/data/mancardhtml?id=2', headers=headers, allow_redirects=False, timeout=30)
except requests.exceptions.RequestException:    # ConnectionError RequestException 
    pass

if(r.status_code != 200):
	print(r.status_code)
	exit()

r.encoding = 'utf-8'
json_str = r.text.replace("\\x22","\\\"").replace("\\r\\n","").replace("	", "  ")

html = json.loads(json_str)['html']
bs = BeautifulSoup(html, 'html.parser')

# 写法一
#for t in bs.find_all("a", class_="title-content"):
#    print(urllib.parse.unquote(t.attrs["href"])," ",t.string)

# 写法二
#for t in bs.select('.title-content'):
#    print(urllib.parse.unquote(t['href']),t.string)

more_json_str = bs.textarea.string
news_array = json.loads(more_json_str)['banner']

result = []
for news in news_array:
	# 合成新字典列表
    result.append({'url':urllib.parse.unquote(urllib.parse.unquote(news['url'])),'title':news['title']})

pd.set_option('max_colwidth',100)
pd.set_option('display.width', 200)
table = pd.DataFrame(result)
print(table)


#f = open('d:\\Users\\user\\Desktop\\pytest\\result.txt', 'w', encoding='UTF-8')
#f.write(bs.prettify())
#f.close()
