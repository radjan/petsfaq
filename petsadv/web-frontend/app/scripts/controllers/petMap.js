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
	  marker.setPosition(new google.maps.LatLng(lat, lng));
	};

    $scope.markerItemClick = function (marker) {
      $scope.googleMap.panTo(marker.getPosition());
      checkApi.get(function(result){alert("result check id: " + result.id)}, marker.id);
    }
  	 
	/********nav bar **********/
	$scope.oneAtATime = true;
	$scope.categories = [
		{title:'最近活動點', type:'recent'},
		{title:'歷史活動點', type:'history'},
		{title:'熱門地點', type:'hot'}
	];

	var setMarkerList = function(result){
		var data = result.data;
		var recentMarkers = [];
		for (var i = 0; i < data.length; i++) {
			var myLatlng = new google.maps.LatLng(data[i].location.latitude, data[i].location.longtitude);
			recentMarkers.push(new google.maps.Marker({
			    map: $scope.googleMap,
			    position: myLatlng,
			    title: data[i].title,
                id: data[i].id, // passing id for later use
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
  }]);
