'use strict';

angular.module('webFrontendApp')
  .factory('checkApi', ['httpService', function (httpService) {

    var resultThen = function(result, successFunc) {
        result.then(function(r) {
                      successFunc(r.data);
                    },
                    httpService.getErrorHandleFunc);
    };

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
        resultThen(result, successFunc)
      },
      list: function(successFunc, offset, size){
        var params = {
          'offset': offset,
          'size': size,
          'userid': httpService.getUserId()
        };

        var result = httpService.sendRequest({'api':'check', 'type':'list', 'params':params});
        resultThen(result, successFunc)
      },
      update: function(successFunc, checkId){

      },
      get: function(successFunc, checkId) {
        var result = httpService.sendRequest({
                            api: 'check',
                            type: 'read',
                            url_params: {id: checkId}
                        });
        resultThen(result, successFunc)
      },
    };
  }]);
