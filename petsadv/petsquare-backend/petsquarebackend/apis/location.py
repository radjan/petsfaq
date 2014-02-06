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


class Schema_locations_get(Schema):
    offset = validators.Int(if_missing=0)
    size   = validators.Int(if_missing=100)
    userid =  validators.Int(if_missing=1)

class Schema_locations_post(Schema):
    name        = validators.UnicodeString(if_missing=u'PlaceName')
    description = validators.UnicodeString(if_missing=u'PlaceDescription')
    longtitude  = validators.Number(if_missing=121.5130475)
    latitude    = validators.Number(if_missing=25.040063)
    address     = validators.UnicodeString(if_missing=u'PlaceAddress')
    userid      = validators.Int(if_missing=1)

class Schema_location_put(Schema):
    name        = validators.UnicodeString()
    description = validators.UnicodeString()
    longtitude  = validators.Number()
    latitude    = validators.Number()
    address     = validators.UnicodeString()
    userid      = validators.Int()



@view_defaults(renderer='json')
class LocationAPI(BaseAPI):
    @view_config(route_name='locations', request_method='OPTIONS')
    def location_options(self):
        #self.XHeaders(methods=['POST'])
        self.XHeaders(headers=['Content-Type','Accept'], methods=['POST'])
        return {}

    @view_config(route_name='location', request_method='OPTIONS')
    def location_option(self):
        #self.XHeaders(methods=['PUT','DELETE'])
        self.XHeaders(headers=['Content-Type','Accept'], methods=['PUT','DELETE'])
        return {}

    @view_config(route_name='locations', request_method='GET')
    def locations_list(self):
        """
        list locations
        API: GET /locations
        """
        #for X-domain development
        self.XHeaders()

        #validation
        success, data, code = self.validate(Schema_locations_get)

        if success:
            serv = LocationService(self.request)
            serv_rtn = serv.list(userid=data['userid'], 
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

    @view_config(route_name='location', request_method='GET')
    def location_show(self):
        """
        show location
        API: GET /location/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()

        #validation
        success, data, code = self.validate(Schema_locations_get)

        try:
            #get id from route_path
            locationid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = LocationService(self.request)
            serv_rtn = serv.show(id=locationid)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn


    #TODO: test me!
    @view_config(route_name='locations', request_method='POST')
    def locations_create(self):
        """
        create location
        API: POST /locations
        """
        #for X-domain development
        self.XHeaders()


        #validation
        success, data, code = self.validate(Schema_locations_post)

        if success:
            serv = LocationService(self.request)
            serv_rtn = serv.create(name=data['name'],
                                   description=data['description'],
                                   longtitude=data['longtitude'],
                                   latitude=data['latitude'],
                                   address=data['address'],
                                   userid=data['userid'])
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'', 
                        'info':data, 
                        'code':code, 
                        'success':False}

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    @view_config(route_name='location', request_method='PUT')
    def location_update(self):
        """
        update locations
        API: PUT /location/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()

        #validation
        success, data, code = self.validate(Schema_location_put)

        try:
            #get id from route_path
            locationid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = LocationService(self.request)
            serv_rtn = serv.update(id=locationid, data=data)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    @view_config(route_name='location', request_method='DELETE')
    def location_delete(self):
        """
        delete location
        API: DELETE /location/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()

        #validation
        success, data, code = self.validate(Schema_locations_get)

        try:
            #get id from route_path
            locationid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = LocationService(self.request)
            serv_rtn = serv.delete(id=locationid)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn


def main():
    pass

if __name__ == '__main__':
    main()

