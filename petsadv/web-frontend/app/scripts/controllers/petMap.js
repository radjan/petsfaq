'use strict';
angular.module('webFrontendApp')
  .controller('PetmapCtrl', ['$scope', 'checkApi', '$log',
  	function ($scope, checkApi, $log) {

  	$scope.googleMarkers = [];
 
	$scope.mapOptions = {
    	center: new google.maps.LatLng(23.5, 121),
		zoom: 8,
		mapTypeId: google.maps.MapTypeId.ROADMAP
    };
	 
	$scope.addMarker = function($event, $params) {
		$scope.googleMarkers.push(new google.maps.Marker({
			map: $scope.googleMap,
			position: $params[0].latLng,
		}));
	};
	 
	$scope.setZoomMessage = function(zoom) {
		$scope.zoomMessage = 'You just zoomed to '+zoom+'!';
	 	console.log(zoom,'zoomed');
	};
	 
	$scope.openMarkerInfo = function(marker) {
		$scope.currentGoogleMarker = marker;
		$scope.currentGoogleMarkerLat = marker.getPosition().lat();
		$scope.currentGoogleMarkerLng = marker.getPosition().lng();
		$scope.currentGoogleMarkerTitle = marker.getTitle();
		$scope.currentGoogleInfoWindow.open($scope.googleMap, marker);

		$scope.currentCheck = $scope.checksInfo[marker.index];
	};
	 
	$scope.setMarkerPosition = function(marker, lat, lng) {
		var config = {};
		config['title'] = $scope.currentGoogleMarkerTitle;
		config['description'] = marker.description;
		config['locationId'] = marker.locationId;
		config['imageId'] = marker.imageId;
		config['id'] = marker.id;

		checkApi.update(config, function(result){
			$log.info('Update marker status: '+result.info.status + ', msg: '+result.info.msg);
			$scope.checksInfo[marker.index].title = $scope.currentGoogleMarkerTitle;
			marker.title = $scope.currentGoogleMarkerTitle;
			marker.setPosition(new google.maps.LatLng(lat, lng));	
		});
		
	};

    $scope.markerItemClick = function (marker) {
      $scope.googleMap.panTo(marker.getPosition());
      $scope.openMarkerInfo(marker);
      // checkApi.get(function(result){alert("result check id: " + result.id)}, marker.id);
    }
  	 
	/********nav bar **********/
	$scope.oneAtATime = true;
	$scope.categories = [
		{title:'最近活動點(check view)', type:'recent'},
		{title:'歷史活動點', type:'history'},
		{title:'熱門地點(location view)', type:'hot'}
	];

	var setMarkerList = function(result){
		var recentMarkers = [];
		var data = result.data;
		for (var i = 0; i < data.length; i++) {
			var myLatlng = new google.maps.LatLng(data[i].location.latitude, data[i].location.longtitude);
			recentMarkers.push(new google.maps.Marker({
			    'map': $scope.googleMap,
			    'index': i,
			    'position': myLatlng,
                'id': data[i].id, // passing id for later use
                'title': data[i].title,
                'description': data[i].description,
                'locationId': data[i].location.id,
                'imageId': data[i].image.id
			 }));
			
		}
		$scope.googleMarkers = recentMarkers;
		$scope.checksInfo = data;
	};

	$scope.setMarkers = function (type){
		if (type === 'recent') {
			var config = {};
			config['offset'] = 0;
			config['size'] = 200;
			checkApi.list(config, setMarkerList);
		} else if (type === 'history'){
			$scope.googleMarkers = [];
		} else if (type === 'hot'){
			$scope.googleMarkers = [];
		}
	};

	// $scope.testPost = function(){
	// 	checkApi.create(testPostCB);
	// };

	// var testPostCB = function(data){
	// 	alert(data);
	// };
  }]);
