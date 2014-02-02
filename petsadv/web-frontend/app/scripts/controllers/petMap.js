'use strict';
angular.module('webFrontendApp')
  .controller('PetmapCtrl', ['$scope', 'checkApi',
  	function ($scope, checkApi) {

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
	};
	 
	$scope.setMarkerPosition = function(marker, lat, lng) {

		checkApi.update(setMarkerPositionCB, marker.id, marker.title, marker.description, marker.locationId, marker.imageId);
		marker.setPosition(new google.maps.LatLng(lat, lng));
	};

	var setMarkerPositionCB = function(data){
		alert("success!");
	};

    $scope.markerItemClick = function (marker) {
      $scope.googleMap.panTo(marker.getPosition());
      $scope.openMarkerInfo(marker);
      // checkApi.get(function(result){alert("result check id: " + result.id)}, marker.id);
    }
  	 
	/********nav bar **********/
	$scope.oneAtATime = true;
	$scope.categories = [
		{title:'最近活動點', type:'recent'},
		{title:'歷史活動點', type:'history'},
		{title:'熱門地點', type:'hot'}
	];

	var setMarkerList = function(data){
		var recentMarkers = [];
		for (var i = 0; i < data.length; i++) {
			var myLatlng = new google.maps.LatLng(data[i].location.latitude, data[i].location.longtitude);
			recentMarkers.push(new google.maps.Marker({
			    map: $scope.googleMap,
			    position: myLatlng,
                id: data[i].id, // passing id for later use
                title: data[i].title,
                description: data[i].description,
                locationId: data[i].location.id,
                imageId: data[i].image.id
			 }));
			
		}
		$scope.googleMarkers = recentMarkers;
		$scope.checksInfo = data;
	};

	$scope.setMarkers = function (type){
		if (type === 'recent') {
			checkApi.list(setMarkerList);
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
