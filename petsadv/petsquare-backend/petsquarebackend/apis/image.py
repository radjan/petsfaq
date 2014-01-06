#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 13, 2013 '
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
from petsquarebackend.services.image import ImageService

from pyramid.response import FileResponse
from pyramid.response import Response
import Image as PILImage

class Schema_images_get(Schema):
    offset = validators.Int(if_missing=0)
    size   = validators.Int(if_missing=100)
    userid =  validators.Int(if_missing=1)

class Schema_images_post(Schema):
    description = validators.UnicodeString()
    image       = validators.FieldStorageUploadConverter() 
    userid      = validators.Int()

class Schema_imagedata_put(Schema):
    description = validators.UnicodeString()
    image       = validators.FieldStorageUploadConverter() 
    userid      = validators.Int()



@view_defaults(renderer='json')
class ImageAPI(BaseAPI):
    @view_config(route_name='images', request_method='OPTIONS')
    def image_options(self):
        self.XHeaders(methods=['POST'])
        return {}

    @view_config(route_name='image', request_method='OPTIONS')
    def image_option(self):
        self.XHeaders(methods=['PUT','DELETE'])
        return {}

    @view_config(route_name='images', request_method='GET')
    def images_list(self):
        """
        list images
        API: GET /images
        """
        #for X-domain development
        self.XHeaders()

        #validation
        success, data, code = self.validate(Schema_images_get)

        if success:
            serv = ImageService(self.request)
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

    @view_config(route_name='image', request_method='GET')
    def image_show(self):
        """
        show image
        API: GET /image/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()

        #validation
        success, data, code = self.validate(Schema_images_get)

        try:
            #get id from route_path
            imageid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = ImageService(self.request)
            serv_rtn = serv.show_img(id=imageid)
            api_rtn = serv_rtn['data']

        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }
            api_rtn = self.format_return(serv_rtn)

        return api_rtn


    @view_config(route_name='imagedata', request_method='GET')
    def image_data(self):
        """
        show image data
        API: GET /image/data/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()

        #validation
        success, data, code = self.validate(Schema_images_get)

        try:
            #get id from route_path
            imageid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = ImageService(self.request)
            serv_rtn = serv.show(id=imageid)
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
    @view_config(route_name='images', request_method='POST')
    def images_create(self):
        """
        create image
        API: POST /images
        """
        #for X-domain development
        self.XHeaders(methods=['POST'])
        #image = self.request.params['image']
        #validation
        success, data, code = self.validate(Schema_images_post, body=False)

        if success:
            serv = ImageService(self.request)
            serv_rtn = serv.create(description=data['description'],
                                   image=data['image'],
                                   userid=data['userid'])
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'', 
                        'info':data, 
                        'code':code, 
                        'success':False}

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    @view_config(route_name='image', request_method='PUT')
    def image_update(self):
        """
        update images
        API: PUT /image/data/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()

        #validation
        success, data, code = self.validate(Schema_imagedata_put)

        try:
            #get id from route_path
            imageid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = ImageService(self.request)
            serv_rtn = serv.update(id=imageid, data=data)
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    @view_config(route_name='image', request_method='DELETE')
    def image_delete(self):
        """
        delete image
        API: DELETE /image/<id:\d+>
        """
        #for X-domain development
        self.XHeaders()

        #validation
        success, data, code = self.validate(Schema_images_get)

        try:
            #get id from route_path
            imageid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False

        if success:
            serv = ImageService(self.request)
            serv_rtn = serv.delete(id=imageid)
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

