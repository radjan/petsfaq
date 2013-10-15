'use strict';

angular.module('hospitalApp')
  .controller('TopnavbarCtrl', function ($scope) {
    $scope.brandName = "Pets FAQ";
    $scope.links = [
        {
            'item': '論壇', 
            'url': '#/knowledge'
        },{
            'item': '找尋醫院',
            'url': '#/hospitalList'
        },{
            'item':'聯絡我們',
            'url': '#/about'
        }
    ];

  });
