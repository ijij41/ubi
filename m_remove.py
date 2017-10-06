#! /usr/bin/python
# -*- coding: utf-8 -*-

import os,urllib
import urllib2
#import mechanize
from urllib2 import urlopen
#from ClientForm import ParseResponse
#from ClientForm import HTMLForm 
import ClientForm
import datetime
import sys
import BeautifulSoup

kiosk_list ={25:'1',87:'2',135:'135',136:'136',137:'137',138:'138',139:'139',140:'140',141:'141'}
kiosk_max_page = {25:4,87:3,135:3,136:3,137:2,138:2,139:4,140:3,141:3}
locker_info={}
oneday_before_locker_info={}

print "Content-type: text/html; charset=EUC-KR\n"



def getRowDataPerPage(kiosk_num,page_num):
	response = urllib2.urlopen('http://www.u-express.com/management/LockerState.asp?page='+str(page_num)+'&colName=Locker_Name&srt=0&kfield=&kword=&srh=0&kid='+str(kiosk_num),timeout=5)
	soup = BeautifulSoup.BeautifulSoup(response)
	values = soup.findAll('td',attrs={'class':'ListSubTD'})
	value_list = [ value.text for value in values]



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




	rows = []
	for x in range(0,len(value_list),5):
		rows.append((value_list[x],value_list[x+1],value_list[x+2],value_list[x+3],value_list[x+4]))
		
	return rows




def getKioskData_local(dir_name,kiosk_num):
	result=[]

	for page_num in range(0,kiosk_max_page[kiosk_num]):
		result=result+getRowDataPerPage_local(dir_name,kiosk_num,page_num+1)
	
	return result

############################################################################

dir_name =""
local_dir_state=False

#
#if len(sys.argv)==2:
#	local_dir_state=True	
#	dir_name=sys.argv[1]



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
		oneday_before_locker_info[kiosk_num] = getKioskData_local(oneday_before.strftime('%Y%m%d_08'),kiosk_num)	


#
else:
	assert False

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

tmp_list=[140,135,141,138,137,139,136]
#tmp_list=[140]


mandantory_pickup={}
after_check_pickup={}

for kiosk_num in tmp_list:
	mandantory_pickup[kiosk_num]=[]
	after_check_pickup[kiosk_num]=[]



for kiosk_num in tmp_list:
	#print
	if(kiosk_num==25 or kiosk_num==87):
		continue


	#print "Kiosk : "+kiosk_list[kiosk_num]
	total_cnt=0
	enable_cnt=0
	disable_cnt=0
	used_cnt = 0
	
	for each_row, before_each_row in zip(locker_info[kiosk_num],oneday_before_locker_info[kiosk_num]):
		#print each_row[1]
		total_cnt = total_cnt +1

		if each_row[1]=='enable':
			enable_cnt = enable_cnt +1

		if each_row[1]=='disable':
			disable_cnt = disable_cnt +1


		if each_row[1]=='used':

			used_cnt = used_cnt+1

	

			state=""
		
	
			isSkip=True



			#if int(each_row[4])>30:
			#print each_row[3], each_row[4]
			#if 'DH' in each_row[3] and int(each_row[4])>30:
			if int(each_row[4])>30:
				isSkip=False
				state='mandantory'

			else:


				#if int(each_row[0])%5==0 and (kiosk_num==135 or kiosk_num==140) and int(each_row[4])>5:
				if int(each_row[0])%5==0 and int(each_row[4])>5:
					state ='aftercheck'
					isSkip=False			
							

				if 'DH' in each_row[3] and int(each_row[4])>10:
					state='aftercheck'
					isSkip=False


			
#


			if isSkip==True:
				continue
					
				


			
			#print state,each_row[0],each_row[2],each_row[4]
			if(state=='mandantory'):
				str_man = each_row[0],each_row[2],each_row[4]
				mandantory_pickup[kiosk_num].append(str_man)
				
			elif(state=='aftercheck'):
				str_man = each_row[0],each_row[2],each_row[4]
				after_check_pickup[kiosk_num].append(str_man)
				#print each_row[0],each_row[2],each_row[4]



#print mandantory_pickup
print "<html>"

for kiosk_num in tmp_list:
	print "<p>"
	print "-------------------</br>"
	aa = "Kiosk : "+kiosk_list[kiosk_num]+"</br>"
	print aa.decode('utf-8').encode('euc-kr')
	print "</br>"

	print "mandantory reclaim"
	if(len(mandantory_pickup[kiosk_num])>0):
		for mand in mandantory_pickup[kiosk_num]:
			print mand[0]+" "+mand[1]+" "+mand[2]+"</br>"
	else:
		print "aa"

	print "</br>"	
	print "confirmed reclaim"

	if(len(after_check_pickup[kiosk_num])>0):
		for afterpick in after_check_pickup[kiosk_num]:
			print afterpick[0]+" "+afterpick[1]+" "+afterpick[2]+"</br>"
	else:
		print "aa"

	print "</br>"	
	print "</p>"



print "</html>"
