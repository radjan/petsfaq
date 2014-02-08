'use strict';
angular.module('webFrontendApp')
  .controller('PetmapCtrl', ['$scope', 'checkApi', '$log', '$location',
  	function ($scope, checkApi, $log, $location) {

  	/******** nav bar **********/
	$scope.oneAtATime = true;
	$scope.categories = [
		{title:'最近活動點(check view)', type:'checks'},
		{title:'歷史活動點', type:'history'},
		{title:'熱門地點(location view)', type:'hot'}
	];
	$scope.setMarkers = function (type){
		$location.path($location.path()+'/'+type);
	};


	/******** Map **********/
	$scope.mapOptions = {
    	center: new google.maps.LatLng(23.5, 121),
		zoom: 8,
		mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    $scope.googleMarkers = [];

    $scope.markerItemClick = function (marker) {
      $scope.googleMap.panTo(marker.getPosition());
      // $scope.openMarkerInfo(marker);
      // checkApi.get(function(result){alert("result check id: " + result.id)}, marker.id);
    }
	 
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

  }]);
