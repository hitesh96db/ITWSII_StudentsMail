def loginvalidate():
	import json

        studentinfo = {}

        studentinfo["name"]="Hitesh Sharma";
        studentinfo["rollno"]="201301065";

        studentinfo["batch"]="2K14";

        return json.dumps(studentinfo)


def loginmy():
	if len(request.vars) != 0:
		session["name"] = "None"
		session["email"] = "None"
		return dict(log=request.vars["logout"])
	return dict(log=0)

def passthru():
	session["name"] = request.vars["name"]
	session["email"] = request.vars["email"]
	return "proceed"

def getuser():

	name = session["name"]
	email = session["email"]
	c = db( db.student.email_id == email ).select()
	if len(c) == 0:
		db.student.insert(email_id = email , name = name )
	return "Added to Database!"

def mails():
	form = SQLFORM(db.attachments, formstyle="divs", submit_button="Attach");
	if form.accepts(request, formname=None):
		 pass    
	if session["name"] == "None":
		response.view = 'main/pls.html'
		return dict(form=form)	
	return dict(form=form)

def getid():
	substr = request.vars["id"]
	l = len(substr)
	rows = db(db.student.email_id[:l] == substr ).select()
	s = ""
	for row in rows:
		if s == "":
			s = row.email_id	
		else:
			s = s+" "+row.email_id
	return str(s)

def add_TA():
        TA = {'anish.shankar':'Anish Shankar', 'anurag.soni':'Anurag Soni', 'madhavan.chetlur':'Madhavan Malolan', 'rajeshkumar.gupta':'Rajeshkumar Gupta', 'ayush.minocha':'Ayush Minocha', 'vineet.kumar':'Vineet Kumar', 'ankush.jain':'Ankush Jain', 'mayank.g':'Mayank Gupta', 'swapna.kidambi':'Swapna Kidambi', 'vishrut.mehta':'Vishrut Mehta', 'gaurav.mishra':'Gaurav Mishra'}
        for i in TA:
                c = db(db.student.email_id == i).select();
                if(len(c) == 0):
                        db.student.insert(email_id=i, name=TA[i]);

        d = {}
        rows = db(db.student).select();
        for row in rows:
                d[row.email_id] = row.name;

        return "Added TAs"

def send():

	import time

        sent_time = time.strftime("%H:%M:%S");
        sent_date = time.strftime("%d-%m-%Y");
       
	import gluon.contrib.simplejson
        a = gluon.contrib.simplejson.loads(request.body.read())
	
	d = {}
	d = eval(a["receivers"])
	sentreceivers = ""

        for i in d:
        	c = db(db.student.email_id == d[i]).select();
		if(len(c) == 0):
        	        return "Please enter a valid e-mail address.";

	
	for i in d:
		if a['sub'] == "":
			a['sub'] = "No Subject"
		sentreceivers = sentreceivers+" "+d[i]
        	db.mail.insert(sender_name=a['sender_name'],rec_email=d[i], sender_email=a['send_id'], subject=a['sub'],mail_message=a['msg'], sent_date=sent_date, sent_time=sent_time, tag=a['tag']);
	
	db.sentmail.insert(sender_name=a['sender_name'],receivers=sentreceivers, sender_email=a['send_id'], subject=a['sub'],mail_message=a['msg'], sent_date=sent_date, sent_time=sent_time, tag=a['tag'])      

	m = {}
	rows = db(db.mail).select();

	for i in d:
		b = []
		for row in rows:
                	if row.rec_email == d[i]:
                        	b.append(row.id);
		m[d[i]] = b;
        
	rows = db(db.student).select();
        for i in m:
		for row in rows:
                	if row.email_id == i:
                        	row.update_record(mails=m[i]);
      
	return "Mail Sent!"

def show():
	import json
	ct = 1;
        mails = {};
        user = request.vars['id'];
        row = db(db.student.email_id == user).select(db.student.mails);
        for i in row:
		if i['mails'] == None:
			return str(mails);
                for j in i['mails']:
                   temp = {}
                   temp["send_id"] = j.sender_email
                   temp["sub"] = j.subject
                   temp["msg"] = j.mail_message
                   temp["sent_date"] = j.sent_date
                   temp["sent_time"] = j.sent_time
                   temp["tag"] = j.tag
                   mails[ct] = temp;
		   ct += 1;
        return json.dumps(mails)

def count():
	import json
	c = {'Academics':0, 'Sports':0, 'Events':0, 'Cultural':0, 'Urgent':0, 'Lost/Found':0, 'General':0}
	name = request.get_vars['name'];
	row = db(db.student.email_id == name).select()
	for i in row:	
		a = i.mails
	
	for i in a:
	    if db.mail.id == i:
	        c[db.mail.tag] += 1;

	return json.dumps(c)

def sent():
	import json
	ct = 1
	mails = {}
	eid = request.get_vars['eid']
	rows = db(db.mail.sender_email == eid).select()
	for row in rows:
		d = {}
		d['rec_email'] = row.rec_email
		d['sub'] = row.subject
		d['msg'] = row.mail_message
		d['tag'] = row.tag
		d['time'] = row.sent_time
		d['date'] = row.sent_date
		mails[ct] = d;
		ct += 1
	return json.dumps(mails)

def sentmails():

	import json
	email = request.vars["email"]
	rows = db(db.sentmail.id > 0).select()
	rows = rows.as_list()

        k = [ str(x) for x in range(1,len(rows)+1) ]
	
        js = dict(zip(k,rows))

        return json.dumps(js)


def drafts():
        import time, gluon.contrib.simplejson
        import json

        date = time.strftime("%d-%m-%Y")
        a = gluon.contrib.simplejson.loads(request.body.read())

        receivers = {}

        receivers = eval(a["receivers"])
	rows = db(db.draftmail).select()
	flag = 0
	for i in rows:
		if i.sender_name == a['sender_name'] and i.receivers == receivers and i.sender_email == a['send_id'] and i.subject == a['sub'] and i.mail_message == a['msg']:
			return "already"

  	db.draftmail.insert(sender_name=a['sender_name'],receivers=receivers, sender_email=a['send_id'], subject=a['sub'],mail_message=a['msg'], made_date=date, tag=a['tag'])
        return "Message Saved to Drafts!"


def getdrafts():

        import time, gluon.contrib.simplejson
        import json
        send_id = request.vars["email"]

        rows = db( db.draftmail.sender_email == send_id ).select()
	rows = rows.as_list()
	
	k = [ x for x in range(1,len(rows)+1) ]
	
	js = dict(zip(k,rows))	
       
	return json.dumps(js)

def checkdrafts():
	import time, gluon.contrib.simplejson
        import json

        date = time.strftime("%d-%m-%Y")
        a = gluon.contrib.simplejson.loads(request.body.read())

        receivers = {}
        receivers = eval(a['receivers'])
	
	db((db.draftmail.sender_name == a['sender_name'] )&(db.draftmail.receivers == receivers)&(db.draftmail.sender_email == a['send_id'])&(db.draftmail.subject == a['sub'] ) &( db.draftmail.mail_message == a['message'])).delete()
        
	return "draft message deleted!"

def deletedrafts():
	
	import time, gluon.contrib.simplejson
	whole = gluon.contrib.simplejson.loads(request.body.read())
		
	for i in whole:
	
		k = {}
		k = eval(whole[i])
	
		db((db.draftmail.sender_name == k['sender_name'] )&(db.draftmail.receivers == k["receivers"])&(db.draftmail.sender_email == k['sender_email'])&(db.draftmail.subject == k['subject'] ) &( db.draftmail.mail_message == k['mail_message'])).delete()

        return "Deleted from Drafts!"	
