#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 08, 2014 '
__author__= 'rad'

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
from petsquarebackend.apis import BaseAPP
from petsquarebackend.services.mission import MissionService


class SchemaMissionsGet(Schema):
    offset = validators.Int(if_missing=0)
    size   = validators.Int(if_missing=100)
    #reporter_id = validators.Int(if_missing=1)

class SchemaMissionPost(Schema):
    name        = validators.UnicodeString(if_missing=u'MissionName')
    type        = validators.UnicodeString(if_missing=u'type')
    status      = validators.UnicodeString(if_missing=u'help')
    description = validators.UnicodeString(if_missing=u'')
    places      = validators.UnicodeString(if_missing=u'')
    note        = validators.UnicodeString(if_missing=u'')
    reporter_id = validators.Int(if_missing=1)
    animal_id   = validators.Int(if_missing=1)

class SchemaMissionPut(Schema):
    id          = validators.Int()
    name        = validators.UnicodeString()
    type        = validators.UnicodeString()
    status      = validators.UnicodeString()
    description = validators.UnicodeString()
    places      = validators.UnicodeString()
    note        = validators.UnicodeString()
    reporter_id = validators.Int()
    animal_id   = validators.Int()

class BaseMission(object):
    """
    For Inheritance only
    """
    def _missions_list(self):
        """
        list missions
        API: GET /missions
        """
        #validation
        success, data, code = self.validate(SchemaMissionsGet)

        if success:
            serv = MissionService(self.request)
            serv_rtn = serv.list(offset=data['offset'],
                                 size=data['size'])
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'', 
                        'info':data, 
                        'code':code, 
                        'success':False}

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _mission_show(self):
        """
        show mission
        API: GET /mission/<id:\d+>
        """
        #validation
        success, data, code = self.validate(SchemaMissionsGet)

        try:
            #get id from route_path
            mission_id = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = MissionService(self.request)
            serv_rtn = serv.show(id=mission_id)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _missions_create(self):
        """
        create mission
        API: POST /missions
        """
        #validation
        success, data, code = self.validate(SchemaMissionPost)

        if success:
            serv = MissionService(self.request)
            data['reporter_id'] = data.pop['user_id']
            serv_rtn = serv.create(**data)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'', 
                        'info':data, 
                        'code':code, 
                        'success':False}

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _mission_update(self):
        """
        update missions
        API: PUT /mission/<id:\d+>
        """
        #validation
        success, data, code = self.validate(SchemaMissionPut)

        try:
            #get id from route_path
            mission_id = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = MissionService(self.request)
            serv_rtn = serv.update(id=mission_id, data=data)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _mission_delete(self):
        """
        delete mission
        API: DELETE /mission/<id:\d+>
        """
        #validation
        success, data, code = self.validate(SchemaMissionsGet)

        try:
            #get id from route_path
            mission_id = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = MissionService(self.request)
            serv_rtn = serv.delete(id=mission_id)
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
class MissionAPI(BaseAPI, BaseMission):
    @view_config(route_name='missions', request_method='OPTIONS')
    def mission_options(self):
        #self.XHeaders(methods=['POST'])
        self.XHeaders(headers=['Content-Type','Accept'], methods=['POST'])
        return {}

    @view_config(route_name='mission', request_method='OPTIONS')
    def mission_option(self):
        #self.XHeaders(methods=['PUT','DELETE'])
        self.XHeaders(headers=['Content-Type','Accept'], methods=['PUT','DELETE'])
        return {}

    @view_config(route_name='missions', request_method='GET')
    def missions_list(self):
        """
        list missions
        API: GET /missions
        """
        #for X-domain development
        self.XHeaders()
        return self._missions_list()

    @view_config(route_name='mission', request_method='GET')
    def mission_show(self):
        """
        show mission
        API: GET /mission/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()
        return self._mission_show()

    #TODO: test me!
    @view_config(route_name='missions', request_method='POST')
    def missions_create(self):
        """
        create mission
        API: POST /missions
        """
        #for X-domain development
        #self.XHeaders(methods=['POST'])
        self.XHeaders()
        return self._missions_create()

    @view_config(route_name='mission', request_method='PUT')
    def mission_update(self):
        """
        update missions
        API: PUT /mission/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()
        self._mission_update()

    @view_config(route_name='mission', request_method='DELETE')
    def mission_delete(self):
        """
        delete mission
        API: DELETE /mission/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()
        self._mission_delete()

@view_defaults(renderer='json')
class MissionAPP(BaseAPP, BaseMission):
    @view_config(route_name='app-missions', request_method='GET')
    def missions_list(self):
        return self._missions_list()

    @view_config(route_name='app-missions', request_method='POST')
    def missions_create(self):
        return self._missions_create()

    @view_config(route_name='app-mission', request_method='GET')
    def mission_show(self):
        return self._mission_show()

    @view_config(route_name='app-mission', request_method='PUT')
    def mission_update(self):
        return self._mission_update()

    @view_config(route_name='app-mission', request_method='DELETE')
    def mission_delete(self):
        return self._mission_delete()


def main():
    pass

if __name__ == '__main__':
    main()

