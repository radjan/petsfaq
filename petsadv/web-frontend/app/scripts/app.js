'use strict';

angular.module('webFrontendApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'ui.bootstrap',
  'ui.map',
  'ezfb',
  'ui.router'
])
  .config(function ($stateProvider, $urlRouterProvider, $httpProvider, $FBProvider) {
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];

    $FBProvider.setInitParams({
      // appId : '670257916371189',
      // channelUrl :'72e3cd86ab5e6fa4b680273374705beb',
      appId      : '365022226968758', // App ID
      channelUrl : 'efecb3e99c55926533debed6c33e63c5', // Channel File
      status     : true, // check login status
      cookie     : true, // enable cookies to allow the server to access the session
      xfbml      : true  // parse XFBML
    });

    $urlRouterProvider.otherwise('/index');

    $stateProvider
      .state('main', {
        url: '/index',
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .state('petMap',{
        url: '/petMap',
        templateUrl: 'views/petMap.html',
        controller: 'PetmapCtrl',
      })
      .state('petMap.checks',{
        url: '/:mapMarkerType',
        templateUrl: 'views/petMapChecks.html',
        resolve: {
          checks : function(checkApi){
            var config = {};
            config['offset'] = 0;
            config['size'] = 200;
            return checkApi.list(config, function(r){ 
                return r;
            });
          }
        },
        controller: 'PetmapchecksCtrl'
      });
    // $routeProvider
    //   .when('/', {
    //     templateUrl: 'views/main.html',
    //     controller: 'MainCtrl'
    //   })
    //   .when('/register', {
    //     templateUrl: 'views/register.html',
    //     controller: 'RegisterCtrl'
    //   })
    //   .when('/petMap', {
    //     templateUrl: 'views/petMap.html',
    //     controller: 'PetmapCtrl'
    //   })
    //   // .when('/login', {
    //   //   templateUrl: 'views/login.html',
    //   //   controller: 'LoginCtrl'
    //   // })
    // .when('/petMapChecks', {
    //   templateUrl: 'views/petMapChecks.html',
    //   controller: 'PetmapchecksCtrl'
    // })
    //   .otherwise({
    //     redirectTo: '/'
    //   });
  });
