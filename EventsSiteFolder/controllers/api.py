# Here go your api methods.

import datetime
from dateutil.parser import parse #for datetime processing from js.
import json #for logger

#for default_index get events

def get_events():
    logger.info("Hi, getting events.")

    events = db(db.events).select().as_list()

    #we also need to get each image actually downloaded...
    for event in events:
        if event['event_image'] is None:
            event['image_src'] = None
        else:
            # inline replacement for <img src="{{=URL('default', 'download', args=picture_name)}}" />
            event['image_src'] = URL('default', 'download', args=event['event_image'])


    logger.info(events)

    # datetime not json serializable.
    # logger.info(json.dumps(events, indent=4, sort_keys=True))

    return response.json(dict(events=events))


#for create event
@auth.requires_signature()
def add_event():
    print("Hi. I am inserting an event.")

    # Parse data.
    # e_name: eventname,
    # e_host: eventhost,
    # e_radio: eventradio,
    # e_datetime: eventdt,
    # e_maxguests: eventmaxguests,
    # e_desc: eventdescription,
    # e_tags: eventtags,
    # e_loc: eventloc,

    e_name = request.vars.e_name
    e_host = request.vars.e_host

    if request.vars.e_radio in ['True', 'true']:
        e_radio = True
    else:
        e_radio = False

    e_datetime = parse(request.vars.e_datetime) #use imported parser, expects certain formats
    
    e_maxguests = int(request.vars.e_maxguests)

    e_desc = request.vars.e_desc

    e_tags = request.vars.e_tags

    e_loc = request.vars.e_loc
    

    eventid = db.events.insert(
        event_name = e_name,
        event_host = e_host,
        event_max = e_maxguests,
        event_rsvp = e_radio,
        event_datetime = e_datetime,
        event_location = e_loc,
        event_description = e_desc,
        event_image = None,
        event_tags = e_tags,
    )

    return response.json(dict(event_id=eventid))