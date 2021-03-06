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

    $urlRouterProvider.when('/petMap', '/petMap/main');
    $urlRouterProvider.when('/petMap/', '/petMap/main');
    $urlRouterProvider.when('/index', '/petMap/main');

    $urlRouterProvider.otherwise('/index');

    $stateProvider
      .state('main', {
        url: '/index',
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .state('petMap',{
        abstract: true,
        url: '/petMap',
        templateUrl: 'views/petMap.html',
        controller: 'PetmapCtrl',
      })
      .state('petMap.checks', {
        url:'/:checksType',
        views: {
          'leftSide':{
            templateUrl: 'views/petMapLeftSide.html',
          },
          // 'rightSide': {
          //   templateUrl: 'views/petMapRightSide.html', 
          // }
        }
      })
      .state('petMap.detail', {
        url:'/:checksType/:id',
        views: {
          'leftSide': {
            templateUrl: 'views/petMapLeftSide.html', 
          },
          'rightSide': {
            templateUrl: 'views/petMapRightSide.html',
            controller: 'PetmaprightsideCtrl'
          }
        }
      });

    //   .when('/petMapRightSide', {
    //   templateUrl: 'views/petMapRightSide.html',
    //   controller: 'PetmaprightsideCtrl'
    // })
  });
