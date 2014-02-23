'use strict';
angular.module('webFrontendApp')
  .controller('PetmapCtrl', ['$scope', 'checkApi', '$log', '$location', '$stateParams',
  	function ($scope, checkApi, $log, $location, $stateParams) {
    /******** nav bar **********/
    $scope.markers = [];
    $scope.googleMarkers = [];
    $scope.type = 'main';
    $scope.$watch('type', function(){
        $location.url('/petMap/'+ $scope.type);
    });

  	/******** nav bar **********/
	$scope.categories = [
		{title:'最近活動點(check view)', type:'recent'},
		{title:'歷史活動點', type:'history'},
		{title:'熱門地點(location view)', type:'hot'}
	];
	$scope.setMarkers = function (type){
        $scope.googleMarkers = [];
        // if($scope.type === type) return;
        switch(type){
            case $scope.categories[0].type:
                $scope.type = type;
                var params = {
                    offset: 0,
                    size: 200
                };
                checkApi.list(params, function(data){
                    $scope.markers = data.data;
                    for (var i = 0; i < $scope.markers.length; i++) {
                        var marker = $scope.markers[i];
                        $scope.googleMarkers.push(new google.maps.Marker({
                            map: $scope.googleMap,
                            position: new google.maps.LatLng(marker.location.latitude, marker.location.longitude),
                        }));
                    };
                });
                break;
            case $scope.categories[1].type:
                $scope.type = type;
                break;
            case $scope.categories[2].type:
                $scope.type = type;
                break;
            default:
                $scope.type = 'main';     
        }
		// $location.path($location.path()+'/'+type);
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
