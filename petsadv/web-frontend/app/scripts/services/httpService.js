'use strict';

angular.module('webFrontendApp')
  .factory('httpService', ['$http', '$q', function ($http, $q) {
    // var baseUri = "api/v1";
    var baseUri = "http://www.petsfaq.info:6543/api/v1";
    var userid = 1;
    var extendUrl = "";

    var serverApi = {
      //CHECK API
      'check': {
        'create': {
          method: 'POST',
          url: baseUri + '/checks',
        },
        'list': {
          method: 'GET',
          url: baseUri + '/checks',
        },
        'update': {
          method: 'PUT',
          url: baseUri + '/check' + extendUrl,

        },
        'delete': {
          method: 'delete',
          url: baseUri + '/check' + extendUrl,
        },
        'read': {
          method: 'GET',
          url: baseUri + '/check' + extendUrl,
        }
      },

    };

    var errorFunc = function(reason){
      console.log(reason);
    };

    /***
      *Config.api: calling check, location...
      *Config.type: CRUD, create, read, update, delete, list
      Config.params: query in url
      Config.data: body data
      Config.extendUrl: add url afrer origin url
    ***/
    return {
      sendRequest: function(config){
        var send = $q.defer();
        var result = send.promise;
        var request = serverApi[config.api][config.type];
        request['params'] = config.params;
        request['data'] = config.bodyData;
        if (config.extendUrl !== undefined) {
          request['url'] += config.extendUrl;
        }

        $http(serverApi[config.api][config.type]).success(function(result){
          send.resolve(result);
        })
        .error(function(result){
          send.reject(result);
        });

        return result;
      },
      getUserId: function(){
        return userid;
      },
      getErrorHandleFunc: errorFunc,

    };

  }]);
