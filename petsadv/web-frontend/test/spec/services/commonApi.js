'use strict';

describe('Service: commonApi', function () {

  // load the service's module
  beforeEach(module('webFrontendApp'));

  // instantiate service
  var commonApi;
  beforeEach(inject(function (_commonApi_) {
    commonApi = _commonApi_;
  }));

  it('should do something', function () {
    expect(!!commonApi).toBe(true);
  });

});
