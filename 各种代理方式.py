#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'代理'

__author__ = 'Lyu'

import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import ssl

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
'authority': 'www.google.com',
'scheme': 'https',
'path': '/',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'upgrade-insecure-requests': '1',
'accept-encoding': 'gzip, deflate, sdch',
'accept-language': 'zh-CN,zh;q=0.8',
'cache-control':'max-age=0',
'cookie': 'SID=6wULX-9_Px5BrfSFbDEVF8IGn5o7xPh9suzEZKj-JFT-Gh5eyzZPGF-Svq5ONBWiUGbSIA.; HSID=AV57W_rBXtNaFKDO5; SSID=A1VBylJpCZWZ9unzP; APISID=5vUae9w6sHvhzfF6/A5Y33cFRK3q71El6B; SAPISID=YnkIHFAjoGxIy-m-/Ams1wFv4CR7AuwPdL; OTZ=4325925_24_24__24_; NID=126=kTxZWfBUR2rqam84pCqF4MpA0VESc-DhZNLu5bLK8-NWh5BDzXvDhU99MUvBfG6ukHmiNpph3pPk_oofg2-hxMll7xBkxjidrQR4yqda_mcNyZutTWPw81zV47UGGH910Od6AOh1RBuOTvOiRFBVe3JExF6juXrjIGvZzH5ZvkSD1TVOtiYtGoENJKFAATmuU9SaeDnX-r-OdIgnIGP80-6XZaLJPcPRBBEZh786ai6NVTrFQxnx4MZrl-C2MbYtNrQAH6-NTPtNy4wNy4wBmrMTBlMtJEZsPtOdqZp-7lmZB1vQDt1048ZxAC8tMAWL5Ni7R8FF3kekgrDQUOgzynYYzFhPFzRPG_5Y97ly4FMM8Tx_F1E; 1P_JAR=2018-3-24-2; OGPC=845686784-20:; SIDCC=AAiTGe9BwWFszu8yPmULTfXtduI5T28hNwwUuhQPj0phKszX9TEy_a_Cklrw4IMRt6L0irxrPg8'}

def f_by_requests():
	proxies_socks5 = {'http':'socks5://192.168.62.201:1090','https':'socks5://192.168.62.201:1090'} 


	ssl._create_default_https_context = ssl._create_unverified_context
	s = requests.session()
	s.keep_alive = False
	r = requests.get('https://www.google.com/', headers = headers, proxies = proxies_socks5, verify=False)

	print(r.status_code)

	r.encoding = 'utf-8'
	save_result(r.text)





import socks
import socket
from urllib import request # urllib2

def f_by_socket():
	socks.set_default_proxy(socks.SOCKS5, "192.168.62.201", 1090)
	socket.socket = socks.socksocket
	r = request.urlopen('https://www.google.com')
	print(r.read())


from sockshandler import SocksiPyHandler

def f_by_pysocks():
	opener = request.build_opener(SocksiPyHandler(socks.SOCKS5, "ss.4399doc.com", 1090))
	x = opener.open("https://source.pixiv.net/common/background-slideshow/bundle.js?d254c75c1687037fa95b")
	print(x.read())

import subprocess as sp
def ping():
	ping = sp.getstatusoutput("ping ss.4399doc.com")
	print(ping[1])

def save_result(result):
	f = open('d:\\Users\\user\\Desktop\\pytest\\result.txt', 'w', encoding='UTF-8')
	f.write(result)
	f.close()

if __name__=='__main__':
	f_by_pysocks()