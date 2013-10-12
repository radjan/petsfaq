'use strict';

angular.module('hospitalApp')
  .controller('HospitallistCtrl', function ($scope) {
    $scope.hospitals = [
        {
            id:'1',
            name:'Hospital 1'
        },{
            id: '2',
            name: 'Hospital 2'
        }
    ];
  });
