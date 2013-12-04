'use strict';

angular.module('webFrontendApp')
  .controller('PetmapCtrl', function ($scope) {
  	var map;
	function initialize() {
	  var mapOptions = {
	    zoom: 8,
	    center: new google.maps.LatLng(23.5, 121)
	  };
	  map = new google.maps.Map(document.getElementsByClassName('map-canvas')[0],
	      mapOptions);
	};

	$scope.loadMap = function(){
		google.maps.event.addDomListener(window, 'load', initialize);
	};
  });
