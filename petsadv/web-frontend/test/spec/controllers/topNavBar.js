'use strict';

describe('Controller: TopnavbarCtrl', function () {

  // load the controller's module
  beforeEach(module('webFrontendApp'));

  var TopnavbarCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    TopnavbarCtrl = $controller('TopnavbarCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
