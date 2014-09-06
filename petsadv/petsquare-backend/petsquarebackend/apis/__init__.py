#!/usr/bin/env python                                                 
# -*- coding: utf-8 -*- 

import logging
log = logging.getLogger(__name__)

from formencode import Invalid
from pyramid.security import authenticated_userid
from petsquarebackend.common import util

RESERVED = ('offset', 'size', 'order_by', 'desc', 'user_id')
IGNORE = ('ignore',)
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class Base(object):
    # TODO move common logic here
    def _validation_error(self, data, code):
        # mock fake serv_rtn
        return util.return_dict(success=False, data='', info=data, code=code)

class BaseAPI(Base):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def format_return(self, serv_rtn, fcode=500, scode=200):
        """
        Handle status returned from Services
        """
        code = serv_rtn.get('code', None)
        status = serv_rtn
        if status['success'] == True:
            self.request.response.status = code if code is not None else scode
            rtn = {'data': status['data'], 'info': status['info']}
        else:
            self.request.response.status = code if code not in (None,
                                                                200) else fcode
            rtn = {'data': status['data'], 'info': status['info']}
        return rtn

    def validate(self, schema,
                 body=True, GET=False, POST=False, json_body=False):
        """
        Handle params sent from web requests
        """
        if len(self.request.body) == 0:
            body = False
        target_dict = dict()
        try:
            conditions = ((GET,       self.request.GET),
                          (POST,      self.request.POST),
                          (body,      self.request.body),
                          #(json_body, self.request.json_body)
                         )
            for con, var in conditions:
                if con:
                    target_dict.update(dict(var))
           
            data = target_dict
            data = schema.to_python(data)

            #FIXME: 
            #remove the user_id key from the validated result
            data['user_id'] = self.request.authenticated_userid
            rtn = (True, data, 200)

        except Invalid, e:
            errors = e.unpack_errors()
            rtn = (False, errors, 400)
        return rtn

    def XHeaders(self, headers=['X-Requested-With'], origins=['*'],methods=[]):
        header = ''
        for h in headers:
            header = header + ', ' + h
        header = header[2:]
        self.request.response.headers.add('Access-Control-Allow-Headers', header)

        origin = ''
        for o in origins:
            origin = origin + ', ' + o
        origin = origin[2:]
        self.request.response.headers.add('Access-Control-Allow-Origin', origin)

        method = ''
        for m in methods:
            method = method + ', ' + m
        method = method[2:]
        if len(methods) != 0:
            self.request.response.headers.add('Access-Control-Allow-Methods', method)

class BaseAPP(Base):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def format_return(self, serv_rtn, fcode=500, scode=200):
        """
        Handle status returned from Services
        """
        code = serv_rtn.get('code', None)
        status = serv_rtn
        if status['success'] == True:
            self.request.response.status = code if code is not None else scode
            rtn = {'data': status['data'], 'info': status['info']}
        else:
            self.request.response.status = code if code is not None else fcode
            rtn = {'data': status['data'], 'info': status['info']}
        return rtn

    def validate(self, schema,
                 body=True, GET=False, POST=False, json_body=False):
        """
        Handle params sent from web requests
        """
        if len(self.request.body) == 0:
            body = False
        target_dict = dict()
        try:
            conditions = ((GET,       self.request.GET),
                          (POST,      self.request.POST),
                          (body,      self.request.body),
                          #(json_body, self.request.json_body)
                         )
            for con, var in conditions:
                if con:
                    target_dict.update(dict(var))
           
            data = target_dict
            data = schema.to_python(data)

            #FIXME: 
            #remove the user_id key from the validated result
            data['user_id'] = self.request.authenticated_userid
            rtn = (True, data, 200)

        except Invalid, e:
            errors = e.unpack_errors()
            rtn = (False, errors, 400)
        return rtn

    def XHeaders(self, headers=['X-Requested-With'], origins=['*'],methods=[]):
        header = ''
        for h in headers:
            header = header + ', ' + h
        header = header[2:]
        self.request.response.headers.add('Access-Control-Allow-Headers', header)

        origin = ''
        for o in origins:
            origin = origin + ', ' + o
        origin = origin[2:]
        self.request.response.headers.add('Access-Control-Allow-Origin', origin)

        method = ''
        for m in methods:
            method = method + ', ' + m
        method = method[2:]
        if len(methods) != 0:
            self.request.response.headers.add('Access-Control-Allow-Methods', method)


