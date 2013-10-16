'use strict';

angular.module('hospitalApp')
  .controller('TopnavbarCtrl', function ($scope) {
    $scope.brandName = "Pets FAQ";
    $scope.links = [
        {
            'item': '論壇', 
            'url': '#/knowledge',
            'isActive':''
        },{
            'item': '找尋醫院',
            'url': '#/hospitalList',
            'isActive':''
        },{
            'item':'聯絡我們',
            'url': '#/about',
            'isActive':''
        }
    ];

    $scope.markActive = function (index){
        var i = 0;
        for(i=0; i<$scope.links.length; i++){
            if(i == index){
                $scope.links[i].isActive = "active";
            }else{
                $scope.links[i].isActive = "";
            }
        }
    };

  });
