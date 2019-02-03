import '../../../base_templates/frontend_partials/js/main.js';
import 'bootstrap/js/dist/carousel';
import 'jquery-parallax.js';
import 'waypoints/lib/jquery.waypoints.js';
import 'jquery-countup';

var $counters = $('#counter .counter_field');
var inits = {
    customers: {
        start: 0,
        last: 1672,
        duration: 1000,
        frame: 1000 / 30
    },
    classes: {
        start: 0,
        last: 124,
        duration: 1000,
        frame: 1000 / 30
    },
    calories: {
        start: 0,
        last: 58325,
        duration: 1000,
        frame: 1000 / 30
    },
    instructors: {
        start: 0,
        last: 16,
        duration: 1000,
        frame: 1000 / 30
    }
};

$('.parallax-window').parallax({
    speed: 0.6
});

$counters.each(function(){
    var $counter = $(this);
    var field = $counter.data('id');
    var init = inits[field];

    $counter.text(init.last);
    new Waypoint({
        element: $counter,
        handler: function(direction) {
            if(direction === 'down')
                $counter.countUp(init);
        },
        offset: '100%'
    });
});