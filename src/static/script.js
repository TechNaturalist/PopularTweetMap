
function initMap() {
  var options = {
    zoom: 4,
    center: { lat: 41, lng: -102 }
  }

  var map = new google.maps.Map(document.getElementById("map"), options);
  var geocoder = new google.maps.Geocoder();

  let location_string = ''
  let infoWindow = new google.maps.InfoWindow({
    position: { lat: 41, lng: -102 }
  });

  map.addListener("click", (mapsMouseEvent) => {
    infoWindow.close();

    let latLng = mapsMouseEvent.latLng;

    infoWindow = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng,
    });

    /*this gets the actual address*/
    /*  
    geocoder.geocode({
      'latLng': mapsMouseEvent.latLng
    }, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        if(results[0]){
          location_string = results[0].formatted_address;
        }
      }
    }); 
    */

    fetch(`/trends?latitude=${latLng.lat()}&longitude=${latLng.lng()}`)
      .then(response => response.json())
      .then(data => {

        let content_string = '<div id="content">' +
          // '<div id="siteNotice">' +
          // "</div>" +
          // `<h1 id = "placeHeading" class="placeHeading">Trending here: ${data['trending_keyword']}</h1>` +
          // '<div id = "sentimentContent">' +
          // `<p>Positive tweets: ${data['num_positive_tweets']}</p>` +
          // `<p>Negative tweets: ${data['num_negative_tweets']}</p>` +
          // `<p>Topics: ${data.major_topics.join(", ")}</p>` +
          // `<p>Location: Latitude=${latLng.lat()}, Longitude=${latLng.lng()}</p>` +
          // '</div>' +
          '</div>';

        var content_string2 = '<table id="trend-table" style="width:100%">' +
          '<tr>' +
          '<th>Trend</th>' +
          '<th>Positive Tweets</th>' +
          '<th>Negative Tweets</th>' +
          '<th>Topics</th>' +
          '<th>Location</th>' +
          '</tr>';

        for (let trend of data) {
          let row = '<tr>' +
            `<td>${trend['trending_keyword']}</td>` +
            `<td>${trend['num_positive_tweets']}</td>` +
            `<td>${trend['num_negative_tweets']}</td>` +
            `<td>${trend['major_topics'].join(", ")}</td>` +
            `<td>Latitude=${latLng.lat()}, Longitude=${latLng.lng()}</td>` +
            '</tr>';
          content_string2 += row;
        }

        content_string2 += "</table>"

        document.getElementById('data').innerHTML = content_string2;
        infoWindow.setContent(content_string);
        infoWindow.open(map);

      });
  });

}