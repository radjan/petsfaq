'use strict';

angular.module('webFrontendApp')
  .controller('PetmapCtrl', function ($scope) {
  	/********* MOCK DATA **/
  	var USER_ID = '000001';

	var MOCK_LOCATIONS = {
		'0001': {
			'name': 'LOCATION_0001',
			'description': 'one sentence desc',
			'lat': 25.04171, //float
			'lng': 121.548353, //float
			'address': 'Taipei City',
		},
		'0002': {
			'name': 'LOCATION_0002',
			'description': 'one sentence desc',
			'lat': 25.021334,
			'lng': 121.548205,
			'address': 'Taipei City',
		},
	};

	 var MOCK_CHECKINS = [
		{
			'user': USER_ID,
		 	'location': MOCK_LOCATIONS['0001'],
		 	'create': '', //timestamp1
		},
		{
			'user': USER_ID,
		 	'location': MOCK_LOCATIONS['0002'],
		 	'create': '', //timestamp2
		},
	];

	/********* END MOCK DATA **/
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
	  
	};

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


	/********nav bar **********/
	$scope.oneAtATime = true;
	$scope.categories=[
		{title:'最近活動點',content:'test1'},
		{title:'歷史活動點',content:'test2'},
		{title:'熱門地點',content:'test3'},
	]
	
  });
