# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())


def record():
#	form = FORM('To:',INPUT(_name='name', requires=[IS_EMAIL(),IS_NOT_EMPTY()), 
#			'Subject:', INPUT(_name='subject'),
#			'Messsage:', TEXTAREA(_name='message'), INPUT(_type='submit'));
#	if form.accepts(request, session):
#		response.flash="Form Accepted";
#		ajax('check', [],  
	return dict();

import time
def send():
	sent_time = time.strftime("%H:%M:%S");
	sent_date = time.strftime("%d-%m-%Y");
	a = {};
	b = []
	a['id'] = request.get_vars['id'];
	a['sub'] = request.get_vars['sub'];
	a['msg'] = request.get_vars['msg'];
	a['tag'] = request.get_vars['tag'];
	a['send_id'] = request.get_vars['send_id'];
	c = db(db.student.email_id == a['id']).select();
	if(len(c) == 0):
		return "Please enter a valid e-mail address.";
	db.mail.insert(rec_email=a['id'], sender_email=a['send_id'], subject=a['sub'],mail_message=a['msg'], sent_date=sent_date, sent_time=sent_time, tag=a['tag']);
	rows = db(db.mail).select();
	for row in rows:
		if row.rec_email == a['id']:
			b.append(row.id);
	rows = db(db.student).select();
	for row in rows:
		if row.email_id == a['id']:
			row.update_record(mails=b);	
	return dict();

def show():
	mails = {};
	user = request.vars['id'];
	row = db(db.student.email_id == user).select(db.student.mails);
	for i in row:
		for j in i['mails']:
		   temp = {}
		   temp['send_id'] = j.sender_id
		   temp['sub'] = j.subject
		   temp['msg'] = j.mail_message
		   temp['sent_date'] = j.sent_date
		   temp['sent_time'] = j.sent_time
		   temp['tag'] = j.tag
		   mails[j] = temp;
	return mails
