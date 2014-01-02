'use strict';

angular.module('webFrontendApp')
  .factory('apiUrlConstant', function () {
    // var baseUri = "/api/v1";
    var baseUri = "http://www.petsfaq.info:6543/api/v1";

    var url = {
      "CHECKS": baseUri + "/checks"
    };

    return url;
  });
