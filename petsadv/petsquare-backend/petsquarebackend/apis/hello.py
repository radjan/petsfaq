#!/usr/bin/env python                                                 
# -*- coding: utf-8 -*- 

from pyramid.view import view_config
from pyramid.view import view_defaults

from petsquarebackend.apis import BaseAPI

@view_defaults(renderer='json')
class Hello(BaseAPI):
    @view_config(route_name='hello', request_method='GET')
    def list(self):
        rtn_list = ['hello',',','world']
        return rtn_list

