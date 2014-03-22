'use strict';

angular.module('webFrontendApp')
  .controller('PetmaprightsideCtrl', ['$scope', 'commonApi', function ($scope, commonApi) {
  	$scope.localImage = {};
  	$scope.init = function(){
  		if ($scope.$parent.currentCheck === undefined) { return; }
  		var image = $scope.$parent.currentCheck.image;
  		var url = commonApi.getImageUrl(image.id); 
  		$scope.localImage = {
  			id: image.id,
  			name: image.filename,
  			description: image.description,
  			url: url
  		};
  	}

  }]);
