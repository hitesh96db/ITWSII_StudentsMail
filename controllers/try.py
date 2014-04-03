import mechanize
import os
import re	
import json
import sys

br = mechanize.Browser()
br.set_proxies({"ftp":"proxy.iiit.ac.in:8080","http":"proxy.iiit.ac.in:8080"})
br.set_handle_equiv(False)	
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [ ('User-Agent','Firefox') ]

br.open("https://isas.iiit.ac.in/index.php")
response1 = br.response()
	#print response1.geturl()
	#print response1.info()

br.form = list(br.forms())[0]
	#for control in br.form.controls:
	#       print control.name


br["StUdent"] = "************"
br["password"] = "***********"
	#br["rno"]="2013"
	#br["grade"]="A"

response1 = br.submit()
f = open('isas.html', 'w')
k = response1.read()
f.write(k)
f.close()

f = open("isas.html","r")
l = f.readlines()
f = open("isas.html","r")
doc = f.read()

if "Incorrect" in doc:
	print "failure"
	sys.exit()
for i in l:
	if "Name" in i:
 	     line1 = i
	if "Batch" in i:
	     line2 = i
	     break

line1 = line1.strip()
line2 = line2.strip()

pass2 = re.findall("<b>.{1,30}<\/b\>",line1)
name = pass2[0][3:-4].lower().title()
rollno = pass2[1][3:-5]

studentinfo = {}

studentinfo["name"]=name;
studentinfo["rollno"]=rollno;
	
pass2 = re.findall("<b>.{1,30}<\/b\>",line2)
batch = pass2[0][3:-4]
no = pass2[1][3:-4]

studentinfo["batch"]=batch;

print json.dumps(studentinfo)
os.system("rm isas.html")
