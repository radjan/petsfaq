'use strict';
angular.module('webFrontendApp')
  .controller('PetmapCtrl', ['$scope', 'apiUrlConstant', '$http', 
  	function ($scope, apiUrlConstant, $http) {

  	$scope.myMarkers = [];
 
	$scope.mapOptions = {
      center: new google.maps.LatLng(23.5, 121),
      zoom: 8,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
	 
	$scope.addMarker = function($event, $params) {
	  $scope.myMarkers.push(new google.maps.Marker({
	    map: $scope.myMap,
	    position: $params[0].latLng,
	  }));
	};
	 
	$scope.setZoomMessage = function(zoom) {
	  $scope.zoomMessage = 'You just zoomed to '+zoom+'!';
	  console.log(zoom,'zoomed')
	};
	 
	$scope.openMarkerInfo = function(marker) {
	  $scope.currentMarker = marker;
	  $scope.currentMarkerLat = marker.getPosition().lat();
	  $scope.currentMarkerLng = marker.getPosition().lng();
	  $scope.currentMarkerTitle = marker.getTitle();
	  $scope.myInfoWindow.open($scope.myMap, marker);
	};
	 
	$scope.setMarkerPosition = function(marker, lat, lng) {
	  marker.setPosition(new google.maps.LatLng(lat, lng));
	};
  	 

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
			'description': "1",
			'title': "check1",
			'createddatetime': "2013-12-27, 00:32:11",
			'userid': 1,
			'image_id': 1,
			'updateddatetime': "2013-12-27, 00:32:11",
			'location': {
				'name': 'LOCATION_0001',
				'description': 'one sentence desc',
				'lat': 25.04171, //float
				'lng': 121.548353, //float
				'address': 'Taipei City 1',
			},
			'id': 1
		},
		{
			'description': "1",
			'title': "check2",
			'createddatetime': "2013-12-27, 00:32:11",
			'userid': 1,
			'image_id': 1,
			'updateddatetime': "2013-12-27, 00:32:11",
			'location': {
				'name': 'LOCATION_0002',
				'description': 'one sentence desc',
				'lat': 25.021334,
				'lng': 121.548205,
				'address': 'Taipei City 2',
			},
			'id': 2
		},
	];

	/********nav bar **********/
	$scope.oneAtATime = true;
	$scope.categories = [
		{title:'最近活動點', type:'recent'},
		{title:'歷史活動點', type:'history'},
		{title:'熱門地點', type:'hot'}
	];

	$scope.setMarkers = function (type){
		if (type === 'recent') {
			$http.get(apiUrlConstant['CHECKS']).success(function(result){
				//FIXME
				result = MOCK_CHECKINS;
				var recentMarkers = [];
				for (var i = 0; i < result.length; i++) {
					var myLatlng = new google.maps.LatLng(result[i].location.lat, result[i].location.lng);
					recentMarkers.push(new google.maps.Marker({
					    map: $scope.myMap,
					    position: myLatlng,
					    title: result[i].title
					 }));
					
				}
				$scope.myMarkers = recentMarkers;
				$scope.sideMarkers = result;
			});
			
		} else if (type === 'history'){
			$scope.myMarkers = [];
		} else if (type === 'hot'){
			$scope.myMarkers = [];
		}
	};

	/********* END MOCK DATA **/
 //  	var map;
 //  	var myLatlng = new google.maps.LatLng(23.5, 121);


	// $scope.markers = [];
	// $scope.markerData = [
	// 	{
	// 		'lat': 23.5,
	// 		'lng': 121,
	// 		'title': 'title1'
	// 	},
	// 	{
	// 		'lat': 24.5,
	// 		'lng': 123,
	// 		'title': 'title2'
	// 	},
	// ];

	// $scope.test = 'test string';
	// var initialize = function() {
	 
	//   var mapOptions = {
	//     zoom: 8,
	//     /*global google */
	//     center: myLatlng
	//   };

	//   global google 
	//   map = new google.maps.Map(document.getElementsByClassName('map-canvas')[0],
	//       mapOptions);

	//   setMarkers();
	  
	// };

	// var setMarkers = function(){
	// 	// marker.setMap(map);
	//   for (var i = 0; i < $scope.markerData.length; i++) {
	//   	var position = new google.maps.LatLng($scope.markerData[i].lat, $scope.markerData[i].lng);
 //  		var marker = new google.maps.Marker({
	// 		position: position,
	// 		title: $scope.markerData[i].title
	// 	});
	// 	marker.setMap(map);
	// 	addInfoWindow($scope.markerData[i].title, marker);
	//   	$scope.markers.push(marker);
	//   }
	// };

	// var addInfoWindow = function(info, marker){
	// 	google.maps.event.addListener(marker, 'click', function() {
	// 		new google.maps.InfoWindow({
	// 			content: '<div>'+info+'<div>'
	// 		}).open(map, marker);
	// 	});
	// };

	// $scope.loadMap = function(){
	// 	/*global google */
	// 	google.maps.event.addDomListener(window, 'load', initialize());
	// };
  }]);
