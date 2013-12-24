'use strict';

angular.module('webFrontendApp')
  .controller('TopnavbarCtrl', function ($scope) {
    $scope.navBarList = [
      {name:"寵物地圖", url:"/#petMap"}
    ];
    $scope.username="登入";
    $scope.login_check="Facebook 登入";
    $scope.initFb = function(){
      window.fbAsyncInit = function() {
        /*global FB */
        FB.init({
          appId      : '365022226968758', // App ID
          channelUrl : 'efecb3e99c55926533debed6c33e63c5', // Channel File
          //appId      : '447182208718938', // App IDz
          //channelUrl : '7fd7975b33e7c21185d476ae1141314c', // Channel Filez
          status     : true, // check login status
          cookie     : true, // enable cookies to allow the server to access the session
          xfbml      : true  // parse XFBML
        });
      };

      (function(d){
         var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
         if (d.getElementById(id)) {return;}
         js = d.createElement('script'); js.id = id; js.async = true;
         js.src = "//connect.facebook.net/en_US/all.js";
         ref.parentNode.insertBefore(js, ref);
       }(document));
    };

    $scope.loginByFB=function(){
      /*global FB */
  		FB.login(function(response) {
  			
  		    if (response.authResponse) {
  		        // The person logged into your app
  		        FB.api('/me', function(response) {
              $scope.username=response.name ;
              console.log($scope.username);
              $scope.login_check='Facebook登出';
       			 	console.log('Good to see you, ' + response.name + '.');
      			});
  		    } else {
  		        // The person cancelled the login dialog
  		    }
  		});
	   };

  });

    // Additional JS functions here






  // Load the SDK asynchronously
