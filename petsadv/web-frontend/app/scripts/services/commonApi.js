'use strict';

angular.module('webFrontendApp')
  .factory('commonApi', ['httpService', function (httpService) {
    return {
      getImageUrl: function(imageId){
        return httpService.getBaseUri()+"/image/"+imageId;
      },
    };
  }]);
