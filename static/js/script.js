// HTML5 geolocation feature
function showLocation(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
  }
  
  function errorHandler(err) {
    if(err.code == 1) {
      alert("Please allow location in your browser settings.");
    }
    else if(err.code == 2) {
      alert("Error: Location unavailable.");
    }
  }
  
  function getLocation() {
      if (navigator.geolocation) {
        var options = {timeout: 60000};
        navigator.geolocation.getCurrentPosition(showLocation, errorHandler, options);
      }
      else{alert("The browser does not support geolocation.");}
  }