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
          url: baseUri + '/check/{id}',
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
        var request_config = serverApi[config.api][config.type];
        config['method'] = request_config.method;
        config['url'] = request_config.url;
        if (config.url_params !== undefined) {
          for (var k in config.url_params) {
            config['url'] = config.url.replace('{'+k+'}',
                                               config.url_params[k]);
          }
        }

        $http(config)
        .success(function(r){
          send.resolve(r);
        })
        .error(function(r){
          send.reject(r);
        });

        return result;
      },
      getUserId: function(){
        return userid;
      },
      getErrorHandleFunc: errorFunc,

    };

  }]);
