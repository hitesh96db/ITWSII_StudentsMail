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
	if session["name"] == "None":
		response.view = 'main/pls.html'
		return dict()	
	return dict()

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

def attach():
        row = db(db.un).select();
        attachme = db(db.attachments).select();
        mail = db(db.mail).select();
        for i in mail:
                for j in attachme:
                         check = row[0].mail_number
                         if j.uniqueId == check and i.unique_field == check:
                                 i.update_record(attachment=j.id)
        mail = db(db.sentmail).select();
#        for i in mail:
#                for j in attachme:
#                        check = i.sent_time + i.sent_date
#                        if j.uniqueId == check:
#                                i.update_record(attachment=j.id)
        return ""

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

def deletesent():

	import time, gluon.contrib.simplejson
        whole = gluon.contrib.simplejson.loads(request.body.read())

        for i in whole:

                k = {}
                k = eval(whole[i])

                db((db.sentmail.sender_name == k['sender_name'] )&(db.sentmail.receivers == k["receivers"])&(db.sentmail.sender_email == k['sender_email'])&(db.sentmail.subject == k['subject'] )&( db.sentmail.mail_message == k['mail_message'])).delete()

        return "Deleted from Sent!"

def search():

	import json
	ct = 1
	result = {}
	x = request.vars["value"];
	name = request.vars["name"]
	if x == '':
		return json.dumps("None");
	rows = db(db.mail.rec_email == name).select();
	for row in rows:
		if x.lower() in row.subject.lower() or x.lower() in row.sender_email.lower():
	    		mail = {}
	    		mail["subject"] = row.subject
			mail["sender"] = row.sender_email
			mail["sent_date"] = row.sent_date
			mail["tag"] = row.tag
			result[ct] = mail
	    		ct += 1
	return json.dumps(result);

def count():
	import json
	c = {'Academics':0, 'Sports':0, 'Events':0, 'Cultural':0, 'Urgent':0, 'Lost/Found':0, 'General':0}
	name = request.get_vars['name'];
	row = db(db.student.email_id == name).select()
	for r in row:
	    a = r.mails

	for i in a:
	    if db.mail.id == i and db.mail.red == 0:
	    	if c.has_key(i.tag):
			c[i.tag] += 1;	    	
	
	return json.dumps(c)	

def attachment():
        Id = request.vars['id'];
        Smail = db(db.sentmail.id==Id).select()
        if Smail[0].attachment is not None:
                attachId = Smail[0].attachment[0].Name
                link = Smail[0].attachment[0].attachment
                return attachId+">"+link
        return ""
def attachment2():
        Id = request.vars['id'];
        mail = db(db.mail.id==Id).select()
        if mail[0].attachment is not None:
                attachId = mail[0].attachment[0].Name
                link = mail[0].attachment[0].attachment
                return attachId+">"+link
        return ""
def deleteInbox():
        counter = request.vars['count'];
        counter = counter.split(">");
        counter.pop();
        for i in counter:
                row = db(db.mail.id==i).select()
                row[0].update_record(delt=1);
        return ""

def showTrash():
        import json
        ct = 1;
        mails = {};
        user = request.vars['id'];
        row = db(db.student.email_id == user).select(db.student.mails);
        for i in row:
                if i['mails'] == None:
                        return str(mails);
                for j in i['mails']:
                    if j.delt == 1:
                        temp = {}
                        temp["send_id"] = j.sender_email
                        temp["sub"] = j.subject
                        temp["msg"] = j.mail_message
                        temp["sent_date"] = j.sent_date
                        temp["sent_time"] = j.sent_time
                        temp["tag"] = j.tag
                        temp["id"] = j.id
                        mails[ct] = temp;
                        ct += 1;
        return json.dumps(mails)

def attachmentview():

	row = db(db.un).select();

	form = SQLFORM(db.attachments, formstyle="divs", submit_button="Attach", upload=URL('download'), fields=['attachment']);
	if request.vars.attachment is not None and request.vars.attachment != "":
		form.vars.uniqueId = row[0].mail_number
		form.vars.Name = request.vars.attachment.filename
	if form.accepts(request, formname=None):
		 pass 
	return dict(form=form)
