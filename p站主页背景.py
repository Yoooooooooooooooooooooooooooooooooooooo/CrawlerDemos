#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'爬取p站主页背景'

__author__ = 'Lyu'

import json
import socks
import socket
from urllib import request # urllib2
from sockshandler import SocksiPyHandler
from bs4 import BeautifulSoup
import pandas as pd

def write_2_file(b):
	f = open('D:\\images\\img.txt', 'w', encoding='UTF-8')
	f.write(b)
	f.close()

proxie = {'http':'socks5://ss的代理地址', 'https':'socks5://ss的代理地址'}  

opener = request.build_opener(SocksiPyHandler(socks.SOCKS5, "ss.4399doc.com", 1090))
request.install_opener(opener)

header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'p_ab_id=0; p_ab_id_2=3; __utmz=235335808.1520937850.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=235335808.|2=login%20ever=no=1^9=p_ab_id=0=1^10=p_ab_id_2=3=1^11=lang=zh=1; __utmc=235335808; __utma=235335808.1168407987.1520937850.1522305732.1522308217.8; PHPSESSID=f9536256ab08d99dcc42cf949fb12a6e; __utmt=1; __utmb=235335808.6.10.1522308217',
'Host': 'www.pixiv.net',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

response_str = request.urlopen("https://www.pixiv.net").read().decode(encoding = "utf-8")


# :authority: i.pximg.net
# :method: GET
# :path: /img-master/img/2016/06/03/01/55/24/57196809_p0_master1200.jpg
# :scheme: https
# accept: image/webp,image/apng,image/*,*/*;q=0.8
# accept-encoding: gzip, deflate, br
# accept-language: zh-CN,zh;q=0.9
# referer: https://www.pixiv.net/
# user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36

bs = BeautifulSoup(response_str, 'html.parser')
data = bs.select(".json-data")


write_2_file(data[0]['value'])

json_data = json.loads(data[0]['value'])['pixivBackgroundSlideshow.illusts']['landscape']

for jd in json_data:
	header['accept'] = 'image/webp,image/apng,image/*,*/*;q=0.8'
	header['referer'] = 'http://www.pixiv.net/member_illust.php?mode=big&illust_id='+jd['illust_id']+'&page=0'

# 	header={':authority': 'i.pximg.net',
# ':method': 'GET',
# ':path': jd['url']['1200x1200'].split('https://i.pximg.net')[1],
# ':scheme': 'https',
# 'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
# 'accept-encoding': 'gzip, deflate, br',
# 'accept-language': 'zh-CN,zh;q=0.9',
# 'referer':'https://www.pixiv.net/',
# 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

	print(jd['url']['1200x1200'])
	r_img = request.urlopen(jd['url']['1200x1200'], None, header)
	write_2_file(r_img)

# result = []
# for news in news_array:
# 	# 合成新字典列表
#     result.append({'url':urllib.parse.unquote(urllib.parse.unquote(news['url'])),'title':news['title']})

# pd.set_option('max_colwidth',100)
# pd.set_option('display.width', 200)
# table = pd.DataFrame(result)
# print(table)


