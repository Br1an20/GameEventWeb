# Here go your api methods.


@auth.requires_signature()
def add_event():
    event_id = db.event.insert(
        event_name=request.vars.event_name,
        event_host=request.vars.event_host,
    )
    # We return the id of the new post, so we can insert it along all the others.
    return response.json(dict(event_id=event_id))