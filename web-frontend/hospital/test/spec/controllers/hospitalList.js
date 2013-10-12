'use strict';

describe('Controller: HospitallistCtrl', function () {

  // load the controller's module
  beforeEach(module('hospitalApp'));

  var HospitallistCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    HospitallistCtrl = $controller('HospitallistCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
