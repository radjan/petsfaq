'use strict';

angular.module('webFrontendApp')
  .controller('PetmapchecksCtrl', ['$scope',
    function ($scope, checks) {
    // console.log($stateParams.mapMarkerType);
    // console.log(checks);
    
    // var googleMarkers = [];
    // for (var i = 0; i < data.length; i++) {
    //     var myLatlng = new google.maps.LatLng(data[i].location.latitude, data[i].location.longtitude);
    //     googleMarkers.push(new google.maps.Marker({
    //         'map': $scope.googleMap,
    //         'index': i,
    //         'position': myLatlng,
    //         'id': data[i].id, // passing id for later use
    //         'title': data[i].title,
    //         'description': data[i].description,
    //         'locationId': data[i].location.id,
    //         'imageId': data[i].image.id
    //      }));
    // }
    // $scope.$parent.googleMarkers = googleMarkers;


    // $scope.openMarkerInfo = function(marker) {
    //     $scope.currentGoogleMarker = marker;
    //     $scope.currentGoogleMarkerLat = marker.getPosition().lat();
    //     $scope.currentGoogleMarkerLng = marker.getPosition().lng();
    //     $scope.currentGoogleMarkerTitle = marker.getTitle();
    //     $scope.currentGoogleInfoWindow.open($scope.googleMap, marker);

    //     $scope.currentCheck = data[marker.index];
    // };    

  }]);