'use strict';

angular.module('webFrontendApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'ui.bootstrap',
  'ui.map',
  'ezfb'
])
  .config(function ($routeProvider, $httpProvider, $FBProvider) {
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

    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/register', {
        templateUrl: 'views/register.html',
        controller: 'RegisterCtrl'
      })
      .when('/petMap', {
        templateUrl: 'views/petMap.html',
        controller: 'PetmapCtrl'
      })
      // .when('/login', {
      //   templateUrl: 'views/login.html',
      //   controller: 'LoginCtrl'
      // })
      .otherwise({
        redirectTo: '/'
      });
  });
