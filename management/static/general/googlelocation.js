<script>
$(document).ready(function(){
    singleMap('22.751726', '75.893737');//Call generate map function with latitude and longitude on page load
});
https://www.google.com.ng/maps/place/Olatunji+House/@6.5662804,3.365538,19z/data=!4m12!1m6!3m5!1s0x103b8d8849693997:0xd0f49342c4b49b0!2sLegacy+Tutors!8m2!3d6.5655183!4d3.3669722!3m4!1s0x0:0xc7c6eac9923ab56d!8m2!3d6.5662804!4d3.3660851

function singleMap(latitude, longitude) {
    var location = 'Cross Rd, Scheme No.54, Vijay Nagar, Indore, Madhya Pradesh, India 452010';//Define address
    var map = new google.maps.Map(document.getElementById('contact_map'), {
        zoom: 12,
        center: new google.maps.LatLng(latitude, longitude),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });//initialize map and set options

    var infowindow = new google.maps.InfoWindow();
    var marker;
    if (location == "") {
        return false;
    }
    
    //initialize marker
    marker = new google.maps.Marker({
        position: new google.maps.LatLng(latitude, longitude),
        map: map
    });

    marker.setIcon('http://maps.google.com/mapfiles/ms/icons/red-dot.png');//set marker icon
    var i = 0;
    google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
            var str = setMarker(location);
            infowindow.setContent(str);
            infowindow.open(map, marker);
        }
    })(marker, i));
}

//Function for generate marker and show address in marker box
function setMarker(location) {        
    var str = '<div style="width:100%">';
    str += '<div  style="float:left;text-align: center;width:100%;">' + location + '</div>';
    str += '</div>';
    return str;
}
</script>