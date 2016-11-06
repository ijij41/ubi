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

kiosk_list = {25:'덕성여대',87:'동덕여대',135:'강남역 4번출구 B1',136:'정자역',137:'청계산',138:'매헌',139:'판교',140:'강남역 개표소',141:'양재역'}
kiosk_max_page = {25:4,87:3,135:3,136:3,137:2,138:2,139:4,140:3,141:3}




def getContent(kiosk_num,page_num):
	response = urllib2.urlopen('http://www.u-express.com/management/LockerState.asp?page='+str(page_num)+'&colName=Locker_Name&srt=0&kfield=&kword=&srh=0&kid='+str(kiosk_num))
	return response.read()




dir = os.path.dirname("/archive/web/html/ubi/")
os.chdir(dir)

html = open('login.asp')
forms = ClientForm.ParseFile(html,'http://www.u-express.com/login/LoginProc.asp')
form = forms[0]
#print form 


form['id']='dream2011'
form['pwd']='dream'
request = form.click()
response = urllib2.urlopen(request)
#print response.read()


tmp_list = kiosk_list.keys()
tmp_list.sort()

dir_name = datetime.datetime.now().strftime('%Y%m%d_%H') 
print dir_name 


if not os.path.exists("log/"+dir_name):
	os.mkdir("log/"+dir_name)
	for kiosk_num in tmp_list:
		os.mkdir("log/"+dir_name+"/"+str(kiosk_num))


for kiosk_num in tmp_list:
	for page_num in range(0,kiosk_max_page[kiosk_num]):
		#print kiosk_num,"*",page_num+1
		content = getContent(kiosk_num,page_num+1)
		content = content.replace('parent.location.href="/index.asp";','')
		f = open('log/'+dir_name+"/"+str(kiosk_num)+"/"+str(page_num+1)+".html",'w')
		f.write(content)
		f.close()

