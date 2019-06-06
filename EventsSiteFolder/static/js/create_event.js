// This is the js for the default/create_event.html view.

var app = function() {

    var self = {};

    Vue.config.silent = false; // show all warnings

    // Extends an array
    self.extend = function(a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };

    // Enumerates an array. Copied from example code. We start at 1, b/c that's how db ids start.
    var enumerate = function(v) { var k=0; return v.map(function(e) {e._idx = k++;});};


    self.add_event = function() {
        console.log("getting event data");

        eventname = $('#eventnameid').val()
        console.log("event name is " + eventname);

        eventhost = $('#eventhostid').val()
        console.log("event host is " + eventhost);

        eventradio = $('input[name=rsvpradio]:checked', '#vue-div').val()
        console.log("checked rsvp radio button is " + eventradio);

        eventdt = $('#datetime-input').val();

        eventmaxguests = $('#maxguestsid').val();
        if (eventmaxguests.length === 0 ) {
            eventmaxguests = Number.MAX_SAFE_INTEGER; //highest max feasible, order 15 (quadrillion people range)
        }

        console.log("max # of guests is " + eventmaxguests);

        eventdescription = $('#eventdescriptionid').val();
        console.log("description is " + eventdescription);

        //I don't know how to do images... skip/add default.

        eventtags =  $('#tagsid').val()
        console.log("tags are " + eventtags);

        eventloc = $('#locationid').val()
        console.log("location is " + eventloc);



        // Sends the rating to the server.
        $.post(add_event_url, {
            e_name: eventname,
            e_host: eventhost,
            e_radio: eventradio,
            e_datetime: eventdt,
            e_maxguests: eventmaxguests,
            e_desc: eventdescription,
            e_tags: eventtags,
            e_loc: eventloc,
            
        },
        function(data) {
            // console.log("Success.");
            console.log("Hi. Inserted event " + data.eventid);
        });


    }


    // Complete as needed. - add all the vue models
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            search_text: '',
        },
        methods: {
            add_event: self.add_event,
        }

    });







    // once all functions are set up, we're gonna do some stuff
    console.log("Hi.");

    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
