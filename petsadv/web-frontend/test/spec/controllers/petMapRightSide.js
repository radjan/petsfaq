'use strict';

describe('Controller: PetmaprightsideCtrl', function () {

  // load the controller's module
  beforeEach(module('webFrontendApp'));

  var PetmaprightsideCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    PetmaprightsideCtrl = $controller('PetmaprightsideCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
