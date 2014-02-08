'use strict';

describe('Controller: PetmapchecksCtrl', function () {

  // load the controller's module
  beforeEach(module('webFrontendApp'));

  var PetmapchecksCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    PetmapchecksCtrl = $controller('PetmapchecksCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
