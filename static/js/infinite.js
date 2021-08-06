
var infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0],
    handler: function(direction) {

    },
    offset: 'bottom-in-view',

    onBeforePageLoad: function () {
        $('.spinner-load').show();
    },
    onAfterPageLoad: function () {
        $('.spinner-load').hide();
    }

});