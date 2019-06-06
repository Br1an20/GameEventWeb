// This is the js for the default/index.html view.

var app = function() {

    var self = {};

    Vue.config.silent = false; // show all warnings

    // Extends an array
    self.extend = function(a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };

    var enumerate = function(v) { var k=0; return v.map(function(e) {e._idx = k++;});};

    self.get_events = function() {
        console.log("getting event data");



        // Sends the rating to the server.
        $.post(get_events_url, {
        },
        function(data) {
            // console.log("Success.");
            console.log("Done getting events.");
            self.vue.events = data.events
            enumerate(self.vue.events)
            // console.log(self.vue.events)
            
        });


    }



    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            events: []
        },
        methods: {
            get_events: self.get_events
        }

    });


    //when done, get events
    self.get_events();


    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
