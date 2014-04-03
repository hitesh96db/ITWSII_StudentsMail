def loginvalidate():
#	return "email %s password %s" % ( request.vars["email"],request.vars["password"] )
	import mechanize
	import os
	import re
	import json

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


	br["StUdent"] = request.vars["email"]
	br["password"] = request.vars["password"]
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

	studentinfo = {}

	if "Incorrect" in doc:
	        studentinfo["name"] = "unknown"
		return json.dumps(studentinfo)
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

	return json.dumps(studentinfo)


def loginmy():
	db.templogin.truncate()
	if len(request.vars) != 0:
		return dict(log=request.vars["logout"])
	return dict(log=0)

def passthru():
#	db = DAL("sqlite://storage.sqlite")
#	db.define_table("login",Field("Name","string"))
	db.templogin.truncate()
	db.templogin.insert(Name=request.vars["name"],Email=request.vars["email"])
	return "proceed"

def getuser():

	import json
#	db = DAL("sqlite://storage.sqlite")
#	db.define_table("login",Field("Name","string"))
	r = db( db.templogin.id == 1 ).select( db.templogin.Name , db.templogin.Email)
	j = {}
	name = j["name"] = r[0].Name
	email = j["email"] = r[0].Email
	c = db( db.student.email_id == email ).select()
	if len(c) == 0:
		db.student.insert(email_id = email , name = name )
	jj = json.dumps(j)
	return jj

def mails():	
	return dict()

def send():

	import time

        sent_time = time.strftime("%H:%M:%S");
        sent_date = time.strftime("%d-%m-%Y");
        a = {};
        b = []
        a['id'] = request.get_vars['id'];
        a['sub'] = request.get_vars['sub'];
        a['msg'] = request.get_vars['msg'];
        a['tag'] = request.get_vars['tag'];
        a['send_id'] = request.get_vars['send_id'];
	a['sender_name'] = request.vars['sender_name'];
	
        c = db(db.student.email_id == a['id']).select();
        if(len(c) == 0):
                return "Please enter a valid e-mail address.";
        db.mail.insert(sender_name=a['sender_name'],rec_email=a['id'], sender_email=a['send_id'], subject=a['sub'],mail_message=a['msg'], sent_date=sent_date, sent_time=sent_time, tag=a['tag']);
        rows = db(db.mail).select();
        for row in rows:
                if row.rec_email == a['id']:
                        b.append(row.id);
        rows = db(db.student).select();
        for row in rows:
                if row.email_id == a['id']:
                        row.update_record(mails=b);
        return "Mail Sent!"

def show():
        mails = {};
        user = request.vars['id'];
        row = db(db.student.email_id == user).select(db.student.mails);
        for i in row:
                for j in i['mails']:
                   temp = {}
                   temp['send_id'] = j.sender_email
                   temp['sub'] = j.subject
                   temp['msg'] = j.mail_message
                   temp['sent_date'] = j.sent_date
                   temp['sent_time'] = j.sent_time
                   temp['tag'] = j.tag
                   mails[j] = temp;
        return str(mails)
