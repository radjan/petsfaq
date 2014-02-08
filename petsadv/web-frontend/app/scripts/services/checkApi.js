'use strict';

angular.module('webFrontendApp')
  .factory('checkApi', ['httpService', function (httpService) {

    var resultThen = function(result, successFunc) {
        return result.then(successFunc, httpService.getErrorHandleFunc);
    };

    return{
      /**
        create body data: title*, description*, location_id*, image_id*
      **/
      create: function(config, successFunc){
        var bodyData = {};
        bodyData['title'] = config.title;
        bodyData['description'] = config.description;
        bodyData['location_id'] = config.locationId;
        bodyData['image_id'] = config.imageId;
        bodyData['user_id'] = httpService.getUserId();

        var result = httpService.sendRequest({
          'api':'check', 
          'type':'create', 
          'data':bodyData
        });
        return resultThen(result, successFunc);
      },
      /**
        list params: offset, size
      **/
      list: function(config, successFunc){
        var paramStr = {};
        paramStr['offset'] = config.offset;
        paramStr['size'] = config.size;
        paramStr['user_id'] = httpService.getUserId();

        var result = httpService.sendRequest({
          'api':'check', 
          'type':'list', 
          'params':paramStr
        });
        return resultThen(result, successFunc);
      },
      /**
        update body data: title*, description*, location_id*, image_id*
        urlParams: id*
      **/
      update: function(config, successFunc){
        var bodyData = {};
        bodyData['title'] = config.title;
        bodyData['description'] = config.description;
        bodyData['location_id'] = config.locationId;
        bodyData['image_id'] = config.imageId;
        bodyData['user_id'] = httpService.getUserId();

        var result = httpService.sendRequest({
          api:'check',
          type: 'update',
          data: bodyData,
          urlParams: {id:config.id}
        });
        return resultThen(result, successFunc);
      },
      /**
        get urlParams: id*
      **/
      get: function(config, successFunc) {
        var result = httpService.sendRequest({
            api: 'check',
            type: 'read',
            urlParams: {id: config.id}
        });
        return resultThen(result, successFunc);
      },
      /**
        delete urlParams: id*
      **/
      delete: function(config, successFunc){
        var result = httpService.sendRequest({
          api: 'check',
          type: 'delete',
          urlParams: {id: config.id}
        });
        return resultThen(result, successFunc);
      }
    };
  }]);
