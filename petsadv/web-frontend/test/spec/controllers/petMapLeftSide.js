'use strict';

describe('Controller: PetmapleftsideCtrl', function () {

  // load the controller's module
  beforeEach(module('webFrontendApp'));

  var PetmapleftsideCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    PetmapleftsideCtrl = $controller('PetmapleftsideCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
