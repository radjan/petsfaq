'use strict';

describe('Service: apiUrlConstant', function () {

  // load the service's module
  beforeEach(module('webFrontendApp'));

  // instantiate service
  var apiUrlConstant;
  beforeEach(inject(function (_apiUrlConstant_) {
    apiUrlConstant = _apiUrlConstant_;
  }));

  it('should do something', function () {
    expect(!!apiUrlConstant).toBe(true);
  });

});
