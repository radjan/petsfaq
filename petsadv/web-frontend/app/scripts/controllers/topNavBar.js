'use strict';

angular.module('webFrontendApp')
  .controller('TopnavbarCtrl', ['$scope', '$FB', function ($scope, $FB) {
    $scope.navBarList = [
      {name:"寵物地圖", url:"/#petMap"}
    ];
    
    $scope.username="登入";
    $scope.login_check="Facebook 登入";
    updateLoginStatus(updateApiMe);
    
    $scope.logoutByFB = function () {
      $FB.logout(function () {
        updateLoginStatus(updateApiMe);
      });
    };

    $scope.loginByFB=function(){
      $FB.login(function (res) {
        /**
         * no manual $scope.$apply, I got that handled
         */
        if (res.authResponse) {
          updateLoginStatus(updateApiMe);
        }
      }, {scope: 'email,user_likes'});
	   };


    function updateLoginStatus (more) {
      $FB.getLoginStatus(function (res) {
        $scope.loginStatus = res;

        (more || angular.noop)();
      });
    }

    function updateApiMe () {
      if($scope.loginStatus.status === 'connected'){
        $FB.api('/me', function (res) {
          // $scope.apiMe = res;
          $scope.username = res.username;
          $scope.userPicture = "http://graph.facebook.com/"+res.id+"/picture";
          $scope.login_check = "登出";
        });  
      }else{
        $scope.username = "登入";
        $scope.userPicture = "";
        $scope.login_check = "Facebook 登入";
      }
      
    }

  }]);