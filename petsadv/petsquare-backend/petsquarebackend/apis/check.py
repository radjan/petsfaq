#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 26, 2013 '
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
from petsquarebackend.services.check import CheckService


class Schema_checks_get(Schema):
    offset  = validators.Int(if_missing=0)
    size    = validators.Int(if_missing=100)
    user_id = validators.Int(if_missing=1)

class Schema_checks_post(Schema):
    title       = validators.UnicodeString(if_missing=u'CheckTitle')
    description = validators.UnicodeString(if_missing=u'CheckDescription')
    location_id = validators.Int(if_missing=1)
    image_id    = validators.Int(if_missing=1)
    user_id     = validators.Int(if_missing=1)

class Schema_check_put(Schema):
    title       = validators.UnicodeString()
    description = validators.UnicodeString()
    location_id = validators.Int()
    image_id    = validators.Int()
    user_id     = validators.Int()


class BaseCheck(object):
    """
    For Inheritance only
    """
    def _checks_list(self):
        """
        list checks
        API: GET /checks
        """
        #validation
        success, data, code = self.validate(Schema_checks_get)

        if success:
            serv = CheckService(self.request)
            serv_rtn = serv.list(user_id=data['user_id'], 
                                 offset=data['offset'],
                                 size=data['size'])
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'', 
                        'info':data, 
                        'code':code, 
                        'success':False}

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _check_show(self):
        """
        show check
        API: GET /check/<id:\d+>
        """
        #validation
        success, data, code = self.validate(Schema_checks_get)

        try:
            #get id from route_path
            checkid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = CheckService(self.request)
            serv_rtn = serv.show(id=checkid)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn


    def _checks_create(self):
        """
        create check
        API: POST /checks
        """
        #validation
        success, data, code = self.validate(Schema_checks_post)

        if success:
            serv = CheckService(self.request)
            serv_rtn = serv.create(name=data['title'],
                                   description=data['description'],
                                   location_id=data['location_id'],
                                   image_id=data['image_id'],
                                   user_id=data['user_id'])
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'', 
                        'info':data, 
                        'code':code, 
                        'success':False}

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _check_update(self):
        """
        update checks
        API: PUT /check/<id:\d+>
        """
        #validation
        success, data, code = self.validate(Schema_check_put)

        try:
            #get id from route_path
            checkid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = CheckService(self.request)
            serv_rtn = serv.update(id=checkid, data=data)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _check_delete(self):
        """
        delete check
        API: DELETE /check/<id:\d+>
        """
        #validation
        success, data, code = self.validate(Schema_checks_get)

        try:
            #get id from route_path
            checkid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = CheckService(self.request)
            serv_rtn = serv.delete(id=checkid)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

@view_defaults(renderer='json')
class CheckAPI(BaseAPI, BaseCheck):
    @view_config(route_name='checks', request_method='OPTIONS')
    def check_options(self):
        self.XHeaders(headers=['Content-Type','Accept'], methods=['POST'])
        return {}

    @view_config(route_name='check', request_method='OPTIONS')
    def check_option(self):
        self.XHeaders(headers=['Content-Type','Accept'], methods=['PUT','DELETE'])
        return {}

    @view_config(route_name='checks', request_method='GET')
    def checks_list(self):
        """
        list checks
        API: GET /checks
        """
        #for X-domain development
        self.XHeaders()
        return self._checks_list()

    @view_config(route_name='check', request_method='GET')
    def check_show(self):
        """
        show check
        API: GET /check/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()
        return self._check_show()

    #TODO: test me!
    @view_config(route_name='checks', request_method='POST')
    def checks_create(self):
        """
        create check
        API: POST /checks
        """
        #for X-domain development
        self.XHeaders()
        self._checks_create()


    @view_config(route_name='check', request_method='PUT')
    def check_update(self):
        """
        update checks
        API: PUT /check/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()
        self._check_update()

    @view_config(route_name='check', request_method='DELETE')
    def check_delete(self):
        """
        delete check
        API: DELETE /check/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()
        self._check_delete()

def main():
    pass

if __name__ == '__main__':
    main()

