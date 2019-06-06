# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("CMPM 131 test site")
    # redirect(URL('default','home'))
    return dict(message=T('Welcome to web2py!'))

def home():
    response.flash = T("CMPM 131 test site")
    query = db.events
    links = []
    grid = SQLFORM.grid(
        query, 
        field_id = db.events.id, # Useful, not mandatory.
        # if you want to display certain fields
        # fields = [], 

        links = links,
        # And now some generic defaults.
        details=True,
        create=True, editable=True, deletable=True,
        csv=False, 
        user_signature=True, # We don't need it as one cannot take actions directly from the form.
    )
    return dict(grid=grid)

@auth.requires_login()
def profile():
    return dict()

def search():
    return dict()

@auth.requires_login()
def createevent():
    if request.vars.id:
        session.id=request.vars.id
    return dict()

def viewevent():
    return dict()
    

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    logger.info("Trying to download something.")
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


