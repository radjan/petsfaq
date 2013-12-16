'use strict';

angular.module('webFrontendApp')
  .controller('PetmapCtrl', function ($scope) {
  	var map;
  	var myLatlng = new google.maps.LatLng(23.5, 121);


	$scope.markers = [];
	$scope.markerData = [
		{
			'lat': 23.5,
			'lng': 121,
			'title': 'title1'
		},
		{
			'lat': 24.5,
			'lng': 123,
			'title': 'title2'
		},
	];

	$scope.test = 'test string';
	var initialize = function() {
	 
	  var mapOptions = {
	    zoom: 8,
	    /*global google */
	    center: myLatlng
	  };

	  /*global google */
	  map = new google.maps.Map(document.getElementsByClassName('map-canvas')[0],
	      mapOptions);

	  setMarkers();
	  
	}

	var setMarkers = function(){
		// marker.setMap(map);
	  for (var i = 0; i < $scope.markerData.length; i++) {
	  	var position = new google.maps.LatLng($scope.markerData[i].lat, $scope.markerData[i].lng);
  		var marker = new google.maps.Marker({
			position: position,
			title: $scope.markerData[i].title
		});
		marker.setMap(map);
		addInfoWindow($scope.markerData[i].title, marker);
	  	$scope.markers.push(marker);
	  }
	};

	var addInfoWindow = function(info, marker){
		google.maps.event.addListener(marker, 'click', function() {
			new google.maps.InfoWindow({
				content: '<div>'+info+'<div>'
			}).open(map, marker);
		});
	};

	$scope.loadMap = function(){
		/*global google */
		google.maps.event.addDomListener(window, 'load', initialize());
	};

	
  });
