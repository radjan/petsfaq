'use strict';

describe('Service: checkApi', function () {

  // load the service's module
  beforeEach(module('webFrontendApp'));

  // instantiate service
  var checkApi;
  beforeEach(inject(function (_checkApi_) {
    checkApi = _checkApi_;
  }));

  it('should do something', function () {
    expect(!!checkApi).toBe(true);
  });

});
