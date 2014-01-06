'use strict';

angular.module('webFrontendApp')
  .factory('checkApi', ['$http', 'apiUrlConstant',
    function($http, apiUrlConstant) {

      //FIXME MOCK DATA
	  var MOCK_CHECKINS = [
		{
			'description': "1",
			'title': "check1",
			'createddatetime': "2013-12-27, 00:32:11",
			'userid': 1,
			'image_id': 1,
			'updateddatetime': "2013-12-27, 00:32:11",
			'location': {
				'name': 'LOCATION_0001',
				'description': 'one sentence desc',
				'lat': 25.04171, //float
				'lng': 121.548353, //float
				'address': 'Taipei City 1',
			},
			'id': 1
		},
		{
			'description': "1",
			'title': "check2",
			'createddatetime': "2013-12-27, 00:32:11",
			'userid': 1,
			'image_id': 1,
			'updateddatetime': "2013-12-27, 00:32:11",
			'location': {
				'name': 'LOCATION_0002',
				'description': 'one sentence desc',
				'lat': 25.021334,
				'lng': 121.548205,
				'address': 'Taipei City 2',
			},
			'id': 2
		},
	  ];

      var CHECK_API_URL = apiUrlConstant['CHECKS'];

      // Public API here
      return {
        list_checks: function(success, error) {
		  $http.get(CHECK_API_URL)
            .success(function(result) {
              // FIXME ignore result
              success(MOCK_CHECKINS);
            })
            .error(function(data) {
              if (error != undefined) {
                error(data);
              }
            });
          }
      };
  }]);


