'use strict';

angular.module('webFrontendApp')
  .controller('TopnavbarCtrl', function ($scope) {

  });


// Additional JS functions here
  window.fbAsyncInit = function() {
    FB.init({
      appId      : '447182208718938', // App ID
      channelUrl : '7fd7975b33e7c21185d476ae1141314c', // Channel File
      status     : true, // check login status
      cookie     : true, // enable cookies to allow the server to access the session
      xfbml      : true  // parse XFBML
    });
    $('#fb-root a').click(function(){
		FB.login(function(response) {
			console.log(response.status);
		    if (response.authResponse) {
		        // The person logged into your app
		        FB.api('/me', function(response) {
     			 	console.log('Good to see you, ' + response.name + '.');
    			});
		    } else {
		        // The person cancelled the login dialog
		    }
		});
	});
};




  // Load the SDK asynchronously
  (function(d){
     var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement('script'); js.id = id; js.async = true;
     js.src = "//connect.facebook.net/en_US/all.js";
     ref.parentNode.insertBefore(js, ref);
   }(document));