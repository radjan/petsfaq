'use strict';

angular.module('webFrontendApp')
  .controller('PetmapCtrl', function ($scope) {
  	var map;
	function initialize() {
	  var mapOptions = {
	    zoom: 8,
	    /*global google */
	    center: new google.maps.LatLng(23.5, 121)
	  };
	  /*global google */
	  map = new google.maps.Map(document.getElementsByClassName('map-canvas')[0],
	      mapOptions);
	}

	$scope.loadMap = function(){
		/*global google */
		google.maps.event.addDomListener(window, 'load', initialize);
	};
  });
