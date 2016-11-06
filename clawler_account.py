#! /usr/bin/python
# -*- coding: utf-8 -*-


import os,urllib
import urllib2
#import mechanize
from urllib2 import urlopen
from ClientForm import ParseResponse
from ClientForm import HTMLForm 
import ClientForm
import datetime
import urllib,urllib2,cookielib
import BeautifulSoup

kiosk_display_list = [25,87,135,136,137,138,139,140,141]

kiosk_list = {25:'덕성여대',87:'동덕여대',135:'강남역 4번출구 B1',136:'정자역',137:'청계산',138:'매헌',139:'판교',140:'강남역 개표소',141:'양재역'}
kiosk_max_page = {25:4,87:3,135:3,136:3,137:2,138:2,139:4,140:3,141:3}

price_map = {25:0,87:0,135:0,136:0,137:0,138:0,139:0,140:0,141:0}





#dir = os.path.dirname("/home/ijij41/clawler/")
#os.chdir(dir)


 
cj = cookielib.CookieJar()
 
data = urllib.urlencode({
    "id" : "dream2011",
    "pwd" : "dream"
    })
 
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
 
r = opener.open("http://www.u-express.com/login/LoginProc.asp",data)
#print(r.read())

nowtime = datetime.datetime.now()	
now_month = nowtime.strftime('%m')		
r = opener.open("http://www.u-express.com/finance/report/rKioskAnalysisMonth.asp?colName=Kiosk_ID&srt=1&saleType=0&fMonth="+str(now_month)+"&lMonth=&txt_kioskid=00&cktype=all&hdncheck=1")

#html = r.read()
#r = unicode(html,'euc-kr')


dir_name = datetime.datetime.now().strftime('%Y%m%d_%H') 
#print dir_name 


if not os.path.exists("account_log/"+dir_name):
	os.mkdir("account_log/"+dir_name)



content = r.read()
content = content.replace('parent.location.href="/index.asp";','')
f = open('account_log/'+dir_name+"/total_account.html",'w')
f.write(content)
f.close()




#
#
#
#
#
#
#
#
#
