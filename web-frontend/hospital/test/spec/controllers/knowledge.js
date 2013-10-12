'use strict';

describe('Controller: KnowledgeCtrl', function () {

  // load the controller's module
  beforeEach(module('hospitalApp'));

  var KnowledgeCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    KnowledgeCtrl = $controller('KnowledgeCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
