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

PARAMS = ('id', 'name', 'type', 'status', 'animal_id',
          'description', 'place', 'note', 'completed', 'due_time', 'host_id',
          'dest_location_id', 'from_location_id', 'requirement', 'period',
          'skill',)
RESERVED = ('offset', 'size', 'order_by', 'desc', 'user_id')
IGNORE = ('ignore',)
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class SchemaMissionsGet(Schema):
    offset      = validators.Int(if_missing=0)
    size        = validators.Int(if_missing=100)

    type        = validators.UnicodeString(if_missing=IGNORE)
    status      = validators.UnicodeString(if_missing=IGNORE)
    completed   = validators.StringBool(if_missing=IGNORE)
    animal_id   = validators.Int(if_missing=IGNORE)
    reporter_id = validators.Int(if_missing=IGNORE)
    host_id     = validators.Int(if_missing=IGNORE)
    dest_location_id = validators.Int(if_missing=IGNORE)

    from_location_id = validators.Int(if_missing=IGNORE)


class SchemaMissionPost(Schema):
    # required
    name        = validators.UnicodeString()
    type        = validators.UnicodeString()
    status      = validators.UnicodeString()
    animal_id   = validators.Int()
    # optional
    description = validators.UnicodeString(if_missing=IGNORE)
    place      = validators.UnicodeString(if_missing=IGNORE)
    note        = validators.UnicodeString(if_missing=IGNORE)
    completed   = validators.StringBool(if_missing=IGNORE)
    # TODO due_time = validators.DateConverter(month_style='yyyy-mm-dd hh:MM:ss', if_missing=IGNORE)
    due_time    = validators.UnicodeString(if_missing=IGNORE)
    host_id     = validators.Int(if_missing=IGNORE)
    dest_location_id = validators.Int(if_missing=IGNORE)

    from_location_id = validators.Int(if_missing=IGNORE)
    requirement      = validators.UnicodeString(if_missing=IGNORE)
    period           = validators.UnicodeString(if_missing=IGNORE)
    skill            = validators.UnicodeString(if_missing=IGNORE)

    # overwrited in create, valid in update
    reporter_id = validators.Int(if_missing=IGNORE)

class SchemaMissionPut(SchemaMissionPost):
    # required
    id          = validators.Int()

    # allow these attributes, not interested anyway
    reporter    = validators.UnicodeString(if_missing=IGNORE)
    host        = validators.UnicodeString(if_missing=IGNORE)
    animal      = validators.UnicodeString(if_missing=IGNORE)
    createddatetime = validators.UnicodeString(if_missing=IGNORE)
    updateddatetime = validators.UnicodeString(if_missing=IGNORE)
    accepter_assocs = validators.UnicodeString(if_missing=IGNORE)


class BaseMission(object):
    """
    For Inheritance only
    """

    def _validation_error(self, data, code):
        # mock fake serv_rtn
        return {'data':'',
                'info':data,
                'code':code,
                'success':False}

    def _missions_list(self):
        """
        list missions
        API: GET /missions
        """
        #validation
        success, data, code = self.validate(SchemaMissionsGet)

        if success:
            serv = MissionService(self.request)
            params = dict((k, v) for k, v in data.items()
                                    if k in PARAMS and v is not IGNORE)
            serv_rtn = serv.list(params=params,
                                 offset=data['offset'],
                                 size=data['size'])
        else:
            serv_rtn = self._validation_error(data, code)

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
            serv_rtn = self._validation_error(data, code)

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
            params = dict((k, v) for k, v in data.items()
                                    if k in PARAMS and v is not IGNORE)
            params['reporter_id'] = data['user_id']
            # TODO use validator
            if 'due_time' in params:
                params['due_time'] = datetime.strptime(params['due_time'],
                                                       DATETIME_FORMAT)
            serv_rtn = serv.create(**params)
        else:
            serv_rtn = self._validation_error(data, code)

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
            params = dict((k, v) for k, v in data.items()
                                    if k in PARAMS and v is not IGNORE)
            # TODO use validator
            if 'due_time' in params:
                params['due_time'] = datetime.strptime(params['due_time'],
                                                       DATETIME_FORMAT)
            serv = MissionService(self.request)
            serv_rtn = serv.update(id=mission_id, data=params)
        else:
            serv_rtn = self._validation_error(data, code)

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
            serv_rtn = self._validation_error(data, code)

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _my_missions(self):
        """
        list my missions
        API: GET /user/me/missions
        """
        #validation
        success, data, code = self.validate(SchemaMissionsGet)

        if success:
            serv = MissionService(self.request)
            params = dict((k, v) for k, v in data.items()
                                    if k in PARAMS and v is not IGNORE)
            serv_rtn = serv.user_missions(
                                data['user_id'],
                                params,
                                offset=data['offset'],
                                size=data['size'])
        else:
            serv_rtn = self._validation_error(data, code)

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

    @view_config(route_name='my-missions', request_method='GET')
    def my_missions(self):
        #for X-domain development
        self.XHeaders()
        return self._my_missions()

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

    @view_config(route_name='app-my-missions', request_method='GET')
    def my_missions(self):
        return self._my_missions()

def main():
    pass

if __name__ == '__main__':
    main()

