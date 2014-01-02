'use strict';

angular.module('webFrontendApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'ui.bootstrap',
  'ui.map'
])
  .config(function ($routeProvider) {
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
      .otherwise({
        redirectTo: '/'
      });
  });
