#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys 
import subprocess


#ll = os.popen("./should-remove.py")
#ss = ll.readlines()
#print ss[0]
#print ss[1]
#print ss[2]
cmd = "./should-remove.py"
p = subprocess.Popen(cmd)
output, error = p.communicate()
#p.wait()
#hooray=p.stdout.readlines()
#print output 
#print error
