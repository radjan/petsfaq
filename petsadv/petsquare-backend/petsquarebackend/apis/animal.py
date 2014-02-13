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
from petsquarebackend.apis import BaseAPP
from petsquarebackend.services.animal import AnimalService


class Schema_animals_get(Schema):
    offset = validators.Int(if_missing=0)
    size   = validators.Int(if_missing=100)
    finder_id =  validators.Int(if_missing=1)

class Schema_animal_post(Schema):
    name        = validators.UnicodeString(if_missing=u'AnimalName')
    type        = validators.UnicodeString(if_missing=u'type')
    sub_type    = validators.UnicodeString(if_missing=u'sub_type')
    status      = validators.UnicodeString(if_missing=u'help')
    description = validators.UnicodeString(if_missing=u'')
    finder_id   = validators.Int(if_missing=1)

class Schema_animal_put(Schema):
    name        = validators.UnicodeString()
    type        = validators.UnicodeString()
    sub_type    = validators.UnicodeString()
    status      = validators.UnicodeString()
    description = validators.UnicodeString()
    finder_id   = validators.Int()

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
        success, data, code = self.validate(Schema_animals_get)

        if success:
            serv = AnimalService(self.request)
            serv_rtn = serv.list(finder_id=data['finder_id'], 
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

    def _animal_show(self):
        """
        show animal
        API: GET /animal/<id:\d+>
        """
        #validation
        success, data, code = self.validate(Schema_animals_get)

        try:
            #get id from route_path
            animalid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = AnimalService(self.request)
            serv_rtn = serv.show(id=animalid)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _animals_create(self):
        """
        create animal
        API: POST /animals
        """
        #validation
        success, data, code = self.validate(Schema_animals_post)

        if success:
            serv = AnimalService(self.request)
            serv_rtn = serv.create(data)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'', 
                        'info':data, 
                        'code':code, 
                        'success':False}

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _animal_update(self):
        """
        update animals
        API: PUT /animal/<id:\d+>
        """
        #validation
        success, data, code = self.validate(Schema_animal_put)

        try:
            #get id from route_path
            animalid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = AnimalService(self.request)
            serv_rtn = serv.update(id=animalid, data=data)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _animal_delete(self):
        """
        delete animal
        API: DELETE /animal/<id:\d+>
        """
        #validation
        success, data, code = self.validate(Schema_animals_get)

        try:
            #get id from route_path
            animalid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = AnimalService(self.request)
            serv_rtn = serv.delete(id=animalid)
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
        return slef._animal_delete()


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

