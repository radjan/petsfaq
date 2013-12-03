#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
__author__= 'samuel'

import traceback
import json
import logging
log = logging.getLogger(__name__)

import formencode
from formencode import Schema
from formencode import validators

from pyramid.view import (
        view_config,
        view_defaults,
        )

from petsquarebackend.apis import BaseAPI
from petsquarebackend.services.location import LocationService


class schema_locs_get(Schema):
    offset = validators.Int(if_missing=0)
    size   = validators.Int(if_missing=100)

class schema_locs_post(Schema):
    pass

class schema_loc_get(Schema):
    pass

class schema_loc_put(Schema):
    pass

class schema_loc_delete(Schema):
    pass


@view_defaults(renderer='json')
class LocationAPI(BaseAPI):
    @view_config(route_name='locations', request_method='GET')
    def locations_list(self):
        """
        list locations
        API: GET /locations
        """

        #for X-domain development
        self.request.response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
        self.request.response.headers.add('Access-Control-Allow-Origin',  '*')


        serv = LocationService(self.request)
        serv_rtn = serv.list()

        api_rtn = self.handle_serv_rtn(serv_rtn)
        return api_rtn


def main():
    pass

if __name__ == '__main__':
    main()
