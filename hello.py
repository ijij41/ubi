#! /usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import apache
import os
import sys 
import subprocess

def handler(req):
	req.content_type = "text/html"
	req.write("<html>\n")
	req.write("<body>\n")
	req.write("\t<h1>Hello, mod_python!</h1>\n")
	req.write("</body>\n")
	req.write("</html>\n")


def remove(req):
	#cmd = ["./should-remove.py"]
	ll = os.popen("./should-remove.py")
	cc = ll.readlines()
	#cc1 = type(cc[0])
	cc1 = ":xx"
	#print cc[0]
	#p = subprocess.Popen(cmd)
	#p.wait()
	#hooray=p.stdout.readlines()
	ss="aa"
	req.content_type = "text/html"
	req.write("<html>\n")
	req.write("\t<h1>start remove!!</h1>\n")
	req.write(cc1)
	#req.write(unicode(cc1, errors="ignore"))
	#req.write(cc[0])
	req.write("\t<h1>end remove!!</h1>\n")
	req.write("</html>\n")
	
