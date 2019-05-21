# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

import datetime

def get_user_email():
    return None if auth.user is None else auth.user.email

def get_current_time():
    return datetime.datetime.utcnow()

db.define_table('events',
	Field('event_name', default='Event Name'),
	Field('event_host', default=get_user_email()),
	Field('event_max', 'integer'),
	Field('event_rsvp', 'boolean'),
	Field('event_datetime', 'datetime'),
	Field('event_location'),
	Field('event_description', 'text'),
	Field('event_image', 'upload'),
	Field('event_tags'),
)


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
