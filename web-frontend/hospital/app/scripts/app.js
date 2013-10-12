'use strict';

angular.module('hospitalApp', [])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/hospitalList', {
        templateUrl: 'views/hospitalList.html',
        controller: 'HospitallistCtrl'
      })
      .when('/knowledge', {
        templateUrl: 'views/knowledge.html',
        controller: 'KnowledgeCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
