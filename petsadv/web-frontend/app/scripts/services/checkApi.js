'use strict';

angular.module('webFrontendApp')
  .factory('checkApi', ['httpService', function (httpService) {
    return{
      createCheck: function(successFunc, title, desc, locationId, imageId){
        var bodyData = {
          'title': title,
          'description': desc,
          'location_id': locationId,
          'imageId': image_id,
          'userid': httpService.getUserId()
        };

        var result = httpService.sendRequest({'api':'check', 'type':'create', 'data':bodyData});
        result.then(successFunc, httpService.getErrorHandleFunc);
      },
      list: function(successFunc, offset, size){
        var params = {
          'offset': offset,
          'size': size,
          'userid': httpService.getUserId()
        };

        var result = httpService.sendRequest({'api':'check', 'type':'list', 'params':params});
        result.then(successFunc, httpService.getErrorHandleFunc);
      },
      update: function(successFunc, checkId){

      },
      get: function(successFunc, checkId) {
        var result = httpService.sendRequest({
                            api: 'check',
                            type: 'read',
                            url_params: {id: checkId}
                        });
        result.then(successFunc, httpService.getErrorHandleFunc);
      },
    };
  }]);
