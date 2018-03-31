#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'爬取hao123首页的有效导航网址'

__author__ = 'Lyu'

import json
import requests
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
import re

import pymysql


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'}

try:
    r = requests.get('https://www.hao123.com', headers=headers, allow_redirects=False, timeout=30)
except requests.exceptions.RequestException:
	print('error')    

if(r.status_code != 200):
	print(r.status_code)
	exit()

r.encoding = 'utf-8'
bs_response = BeautifulSoup(r.text, 'html.parser')
tags = bs_response.select('#__cnt_0_5')
html = tags[0].string

bs_html = BeautifulSoup(html, 'html.parser')
tags_a = bs_html.select('a')

result = []
result_filter = []

for a in tags_a:
	if(a.string == None):
		continue
	# 过滤hao123的网站
	pattern = re.compile(r'^http(s)?://(\w+).hao123.com(/)?', re.I) #表示忽略大小写
	m = pattern.match(a['href'])
	if(m!=None):
		result_filter.append({'url':a['href'],'title':a.string})
		continue
	result.append({'url':a['href'],'title':a.string})

pd.set_option('max_colwidth',100)
pd.set_option('display.width', 200)
table = pd.DataFrame(result)
# print(table)

db = pymysql.connect(host='localhost', user='root', passwd='root', db='8f', charset='UTF8')
cursor = db.cursor()

for res in result:
	if(res['title']=='新浪' or res['title']=='搜狐体育' or res['title']=='团购'):
		continue
	sql = "INSERT INTO navi_sites(name,  site) VALUES ('%s', '%s')" % (res['title'], res['url'])
	print(sql)
	cursor.execute(sql)

cursor.close()
db.close()


#f = open('d:\\Users\\user\\Desktop\\pytest\\result.txt', 'w', encoding='UTF-8')
#f.write(bs.prettify())
#f.close()
