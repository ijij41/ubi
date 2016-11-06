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
import sys
import BeautifulSoup

kiosk_list = {25:'덕성여대',87:'동덕여대',135:'강남역 4번출구 B1',136:'정자역',137:'청계산',138:'매헌',139:'판교',140:'강남역 개표소',141:'양재역'}
#kiosk_list = {140:'강남역 개표소'}
kiosk_max_page = {25:4,87:3,135:3,136:3,137:2,138:2,139:4,140:3,141:3}
locker_info={}
oneday_before_locker_info={}

print "Content-type: text/html\n"

#def getContent(kiosk_num,page_num):
#	response = urllib2.urlopen('http://www.u-express.com/management/LockerState.asp?page='+str(page_num)+'&colName=Locker_Name&srt=0&kfield=&kword=&srh=0&kid='+str(kiosk_num))
#	return response.read()
#


def getRowDataPerPage(kiosk_num,page_num):
	response = urllib2.urlopen('http://www.u-express.com/management/LockerState.asp?page='+str(page_num)+'&colName=Locker_Name&srt=0&kfield=&kword=&srh=0&kid='+str(kiosk_num),timeout=5)
	soup = BeautifulSoup.BeautifulSoup(response)
	values = soup.findAll('td',attrs={'class':'ListSubTD'})
	value_list = [ value.text for value in values]


#
#	value_list= ['used' if x==u'\xbb\xe7\xbf\xeb\xc1\xdf' else x for x in value_list]
#	value_list= ['enable' if x==u'\xb0\xa1\xb4\xc9' else x for x in value_list]
#	value_list= ['disable' if x==u'\xba\xd2\xb0\xa1' else x for x in value_list]
#


	test_key_used = u'\uc0ac\uc6a9\uc911'
	test_key_enable = u'\uac00\ub2a5'
	test_key_disable = u'\ubd88\uac00'


	if not ((test_key_used in value_list) or (test_key_enable in value_list) or (test_key_disable in value_list)):
		assert False
		
	
	value_list= ['used' if x==test_key_used else x for x in value_list]
	value_list= ['enable' if x==test_key_enable else x for x in value_list]
	value_list= ['disable' if x==test_key_disable else x for x in value_list]



	rows = []
	for x in range(0,len(value_list),5):
		rows.append((value_list[x],value_list[x+1],value_list[x+2],value_list[x+3],value_list[x+4]))
		
	return rows




def getKioskData(kiosk_num):
	result=[]

	for page_num in range(0,kiosk_max_page[kiosk_num]):
		result=result+getRowDataPerPage(kiosk_num,page_num+1)
	
	return result





def getRowDataPerPage_local(dir_name,kiosk_num,page_num):


	f=open('log/'+dir_name+"/"+str(kiosk_num)+"/"+str(page_num)+".html",'r')
	response = f.read()
	f.close()


	soup = BeautifulSoup.BeautifulSoup(response)
	values = soup.findAll('td',attrs={'class':'ListSubTD'})
	value_list = [ value.text for value in values]

#
	test_key_used = u'\uc0ac\uc6a9\uc911'
	test_key_enable = u'\uac00\ub2a5'
	test_key_disable = u'\ubd88\uac00'


	if not ((test_key_used in value_list) or (test_key_enable in value_list) or (test_key_disable in value_list)):
		assert False
		

	
	value_list= ['used' if x==test_key_used else x for x in value_list]
	value_list= ['enable' if x==test_key_enable else x for x in value_list]
	value_list= ['disable' if x==test_key_disable else x for x in value_list]




#	value_list= ['used' if x==u'\xbb\xe7\xbf\xeb\xc1\xdf' else x for x in value_list]
#	value_list= ['enable' if x==u'\xb0\xa1\xb4\xc9' else x for x in value_list]
#	value_list= ['disable' if x==u'\xba\xd2\xb0\xa1' else x for x in value_list]

	rows = []
	for x in range(0,len(value_list),5):
		rows.append((value_list[x],value_list[x+1],value_list[x+2],value_list[x+3],value_list[x+4]))
		
	return rows




def getKioskData_local(dir_name,kiosk_num):
	result=[]

	for page_num in range(0,kiosk_max_page[kiosk_num]):
		result=result+getRowDataPerPage_local(dir_name,kiosk_num,page_num+1)
	
	return result



dir_name =""
local_dir_state=False
#
#
#if len(sys.argv)==2:
#	local_dir_state=True	
#	dir_name=sys.argv[1]
#


if (local_dir_state==False):
	#login 
	#dir = os.path.dirname("/home/ijij41/clawler/")
	#os.chdir(dir)

	dir = os.path.dirname("/archive/web/html/ubi/")
	os.chdir(dir)
	html = open('login.asp')
	forms = ClientForm.ParseFile(html,'http://www.u-express.com/login/LoginProc.asp')
	form = forms[0]
	#print form 
	form['id']='dream2011'
	form['pwd']='dream'
	request = form.click()
	response = urllib2.urlopen(request,timeout=5)
	#print response.read()

	#get all information
	for kiosk_num in kiosk_list.keys():
		locker_info[kiosk_num] = getKioskData(kiosk_num)	


	standard_date = datetime.datetime.now()	
	oneday_before =standard_date - datetime.timedelta(days = 1)	


	#get all information
	for kiosk_num in kiosk_list.keys():
		#oneday_before_locker_info[kiosk_num] = getKioskData_local(oneday_before.strftime('%Y%m%d_08'),kiosk_num)	
		oneday_before_locker_info[kiosk_num] = getKioskData_local(oneday_before.strftime('%Y%m%d_17'),kiosk_num)	


#	for kiosk_num in kiosk_list.keys():
#		print locker_info[kiosk_num]
#		print oneday_before_locker_info[kiosk_num]	
#		break
	#print "end"

else:
	
	#check Dir
	if not os.path.exists("log/"+dir_name):
		print "No exist path", dir_name
		sys.exit(0)	

	#get all information
	for kiosk_num in kiosk_list.keys():
		locker_info[kiosk_num] = getKioskData_local(dir_name,kiosk_num)	


	standard_date = datetime.datetime(int(dir_name[0:4]), int(dir_name[4:6]),int(dir_name[6:8]))
	oneday_before = standard_date - datetime.timedelta(days = 1)	
	

	#get all information
	for kiosk_num in kiosk_list.keys():
		oneday_before_locker_info[kiosk_num] = getKioskData_local(oneday_before.strftime('%Y%m%d_08'),kiosk_num)	





#print results
tmp_list = kiosk_list.keys()
tmp_list.sort()


for kiosk_num in tmp_list:
	print
	
	print "Kiosk : "+str(kiosk_num),"Name : "+kiosk_list[kiosk_num]
	total_cnt=0
	enable_cnt=0
	disable_cnt=0
	used_cnt = 0

	for each_row, before_each_row in zip(locker_info[kiosk_num],oneday_before_locker_info[kiosk_num]):
		# DEBUG
		#print each_row[1]
		#print each_row, each_row[1]
		#print before_each_row, before_each_row[1]
			
	#	if True:
	#		sys.exit(0)

		total_cnt = total_cnt +1

		if each_row[1]=='enable':
		#if "가능" in each_row[1]:
			enable_cnt = enable_cnt +1

		if each_row[1]=='disable':
		#if "불가" in each_row[1]:
			disable_cnt = disable_cnt +1


		if each_row[1]=='used':
		#if "사용" in each_row[1]:

			used_cnt = used_cnt+1

			state=""
			
			if 'DH' in each_row[3] and int(each_row[4])>3:
				state="* [사물함  ] 연체 [수거요망] (물건이 없을 가능성이 큼)"
			
			if 'DH' in each_row[3] and (int(each_row[4])<4 and int(each_row[4])>0):
				state="  [사물함  ] 연체중 (물건이 없을 가능성이 큼)"
		
			if not 'DH' in each_row[3] and int(each_row[4])>3:
				state="!* [일반보관] 연체 [수거요망]" 

			if not 'DH' in each_row[3] and (int(each_row[4])<4 and int(each_row[4])>0):
				state="  [일반보관] 연체중"

					
				


			if 'DH' in each_row[3]:
				locker_due_date = datetime.datetime(int(each_row[3][3:7]), int(each_row[3][7:9]),int(each_row[3][9:11]))
				#print locker_due_date
				today_date = datetime.datetime.now()
				today_only_date = today_date.date()

#				computed_date = locker_due_date + datetime.timedelta(days=int(each_row[4]))
#				print computed_date
				#print today_date.hour	
				if today_date.hour >= 8:
				#if today_date.hour < 8:
					#computed_date = locker_due_date + datetime.timedelta(days=int(each_row[4])-1)
					computed_date = locker_due_date + datetime.timedelta(days=int(each_row[4]))
				else:
					computed_date = locker_due_date + datetime.timedelta(days=int(each_row[4]))
				
				#print today_only_date,locker_due_date, computed_date, each_row[4]
			
				if today_only_date > computed_date.date():
					print today_only_date, computed_date.date()
					state = "  [Some problem Stall] "+state 

				
			
#				if locker_date < today_date and each_row==before_each_row:
#					#state ="초기화 필요"
#					state = state + ""
#
			print each_row," | ",state
			#print each_row
			#print before_each_row,state

	if kiosk_num in [137,138,140]:
		total_cnt = total_cnt - 5 
		disable_cnt = disable_cnt - 5

	print "총 함 갯수 :",total_cnt,"사용 함 개수:",used_cnt,"남은 함갯수 :",enable_cnt,"불가함 갯수 :",disable_cnt



