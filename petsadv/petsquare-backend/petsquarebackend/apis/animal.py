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

from petsquarebackend import apis
from petsquarebackend.apis import BaseAPI
from petsquarebackend.apis import BaseAPP
from petsquarebackend.services.animal import AnimalService

RESERVED = apis.RESERVED
IGNORE = apis.IGNORE
DATETIME_FORMAT = apis.DATETIME_FORMAT

PARAMS = ('id', 'name', 'type', 'sub_type', 'status', 'description', 
          'finder_id', 'owner_id', 'find_location', 'current_location')

class SchemaAnimalsGet(Schema):
    offset = validators.Int(if_missing=0)
    size   = validators.Int(if_missing=100)

    id          = validators.Int(if_missing=IGNORE)
    name        = validators.UnicodeString(if_missing=IGNORE)
    type        = validators.UnicodeString(if_missing=IGNORE)
    sub_type    = validators.UnicodeString(if_missing=IGNORE)
    status      = validators.UnicodeString(if_missing=IGNORE)
    finder_id   = validators.Int(if_missing=IGNORE)
    owner_id    = validators.Int(if_missing=IGNORE)
    find_location_id    = validators.Int(if_missing=IGNORE)
    current_location_id = validators.Int(if_missing=IGNORE)

class SchemaAnimalsPost(Schema):
    # required
    name        = validators.UnicodeString()
    type        = validators.UnicodeString()
    sub_type    = validators.UnicodeString()
    status      = validators.UnicodeString()

    # optional
    description = validators.UnicodeString(if_missing=IGNORE)
    owner_id    = validators.Int(if_missing=IGNORE)
    find_location_id    = validators.Int(if_missing=IGNORE)
    current_location_id = validators.Int(if_missing=IGNORE)

    # overwrited in create, valid in update
    finder_id   = validators.Int(if_missing=IGNORE)

class SchemaAnimalPut(SchemaAnimalsPost):
    # optinal: overwrite
    name        = validators.UnicodeString(if_missing=IGNORE)
    type        = validators.UnicodeString(if_missing=IGNORE)
    sub_type    = validators.UnicodeString(if_missing=IGNORE)
    status      = validators.UnicodeString(if_missing=IGNORE)

    # allow these attributes, not interested anyway
    id          = validators.Int(if_missing=IGNORE)
    finder      = validators.UnicodeString(if_missing=IGNORE)
    owner       = validators.UnicodeString(if_missing=IGNORE)
    find_location   = validators.UnicodeString(if_missing=IGNORE)
    current_location= validators.UnicodeString(if_missing=IGNORE)
    createddatetime = validators.UnicodeString(if_missing=IGNORE)
    updateddatetime = validators.UnicodeString(if_missing=IGNORE)
    accepter_assocs = validators.UnicodeString(if_missing=IGNORE)

class BaseAnimal(object):
    """
    For Inheritance only
    """
    def _animals_list(self):
        """
        list animals
        API: GET /animals
        """
        #validation
        success, data, code = self.validate(SchemaAnimalsGet)

        if success:
            serv = AnimalService(self.request)
            params = dict((k, v) for k, v in data.items()
                                    if k in PARAMS and v is not IGNORE)
            serv_rtn = serv.list(params=params,
                                 offset=data['offset'],
                                 size=data['size'])
        else:
            serv_rtn = self._validation_error(data, code)

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _animal_show(self):
        """
        show animal
        API: GET /animal/<id:\d+>
        """
        #validation
        success, data, code = self.validate(SchemaAnimalsGet)

        try:
            #get id from route_path
            animalid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = AnimalService(self.request)
            serv_rtn = serv.show(id=animalid)
        else:
            serv_rtn = self._validation_error(data, code)

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _animals_create(self):
        """
        create animal
        API: POST /animals
        """
        #validation
        success, data, code = self.validate(SchemaAnimalsPost)

        if success:
            serv = AnimalService(self.request)
            params = dict((k, v) for k, v in data.items()
                                    if k in PARAMS and v is not IGNORE)
            params['finder_id'] = data['user_id']
            serv_rtn = serv.create(params)
        else:
            serv_rtn = self._validation_error(data, code)

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _animal_update(self):
        """
        update animals
        API: PUT /animal/<id:\d+>
        """
        #validation
        success, data, code = self.validate(SchemaAnimalPut)

        try:
            #get id from route_path
            animalid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = AnimalService(self.request)
            params = dict((k, v) for k, v in data.items()
                                    if k in PARAMS and v is not IGNORE)
            serv_rtn = serv.update(id=animalid, data=params)
        else:
            serv_rtn = self._validation_error(data, code)

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _animal_delete(self):
        """
        delete animal
        API: DELETE /animal/<id:\d+>
        """
        #validation
        success, data, code = self.validate(SchemaAnimalsGet)

        try:
            #get id from route_path
            animalid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = AnimalService(self.request)
            serv_rtn = serv.delete(id=animalid)
        else:
            serv_rtn = self._validation_error(data, code)

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

@view_defaults(renderer='json')
class AnimalAPI(BaseAPI, BaseAnimal):
    @view_config(route_name='animals', request_method='OPTIONS')
    def animal_options(self):
        #self.XHeaders(methods=['POST'])
        self.XHeaders(headers=['Content-Type','Accept'], methods=['POST'])
        return {}

    @view_config(route_name='animal', request_method='OPTIONS')
    def animal_option(self):
        #self.XHeaders(methods=['PUT','DELETE'])
        self.XHeaders(headers=['Content-Type','Accept'], methods=['PUT','DELETE'])
        return {}

    @view_config(route_name='animals', request_method='GET')
    def animals_list(self):
        """
        list animals
        API: GET /animals
        """
        #for X-domain development
        self.XHeaders()
        return self._animals_list()

    @view_config(route_name='animal', request_method='GET')
    def animal_show(self):
        """
        show animal
        API: GET /animal/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()
        return self._animal_show()

    #TODO: test me!
    @view_config(route_name='animals', request_method='POST')
    def animals_create(self):
        """
        create animal
        API: POST /animals
        """
        #for X-domain development
        #self.XHeaders(methods=['POST'])
        self.XHeaders()
        return self._animals_create()

    @view_config(route_name='animal', request_method='PUT')
    def animal_update(self):
        """
        update animals
        API: PUT /animal/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()
        return self._animal_update()

    @view_config(route_name='animal', request_method='DELETE')
    def animal_delete(self):
        """
        delete animal
        API: DELETE /animal/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()
        return self._animal_delete()


@view_defaults(renderer='json')
class AnimalAPP(BaseAPP, BaseAnimal):
    @view_config(route_name='app-animals', request_method='GET')
    def animals_list(self):
        return self._animals_list()

    @view_config(route_name='app-animals', request_method='POST')
    def animals_create(self):
        return self._animals_create()

    @view_config(route_name='app-animal', request_method='GET')
    def animal_show(self):
        return self._animal_show()

    @view_config(route_name='app-animal', request_method='PUT')
    def animal_update(self):
        return self._animal_update()

    @view_config(route_name='app-animal', request_method='DELETE')
    def animal_delete(self):
        return self._animal_delete()


def main():
    pass

if __name__ == '__main__':
    main()

