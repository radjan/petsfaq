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
          url: baseUri + '/check/{id}',
        },
        'delete': {
          method: 'delete',
          url: baseUri + '/check/{id}',
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
      Config.api: calling check, location... (String)
      Config.type: CRUD, create, read, update, delete, list (String)
      Config.params: query in url (Object)
      Config.data: body data (Object)
      Config.urlParams: extend url.  (Object)
    ***/
    return {
      sendRequest: function(config){
        var send = $q.defer();
        var result = send.promise;
        var request_config = serverApi[config.api][config.type];
        config['method'] = request_config.method;
        config['url'] = request_config.url;
        if (config.urlParams !== undefined) {
          for (var k in config.urlParams) {
            config['url'] = config.url.replace('{'+k+'}',
                                               config.urlParams[k]);
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
