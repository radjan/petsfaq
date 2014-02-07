#!/usr/bin/env python                                                 
# -*- coding: utf-8 -*- 

import logging
log = logging.getLogger(__name__)

from formencode import Invalid
from pyramid.security import authenticated_userid

class BaseAPI(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def format_return(self, serv_rtn, fcode=500, scode=200):
        """
        Handle status returned from Services
        """
        status = serv_rtn
        if status['success'] == True:
            self.request.status_int = scode
            rtn = {'data': status['data'], 'info': status['info']}
        else:
            self.request.status_int = fcode
            rtn = {'data': status['data'], 'info': status['info']}
        return rtn

    def validate(self, schema, body=True):
        """
        Handle params sent from web requests
        """
        try:
            #log.debug('request param: %s' % self.request.params)
            #log.debug('request body: %s'  % self.request.body)
            target_dict = dict()

            if body == True:
                target_dict.update(dict(self.request.params.copy()))
                if len(self.request.body) > 0:
                    target_dict.update(dict(self.request.json_body.copy()))
            else:
                target_dict.update(dict(self.request.params.copy()))

            data = dict(target_dict)
            data = schema.to_python(data)
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

class BaseAPP(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def format_return(self, serv_rtn, fcode=500, scode=200):
        """
        Handle status returned from Services
        """
        status = serv_rtn
        if status['success'] == True:
            self.request.status_int = scode
            rtn = {'data': status['data'], 'info': status['info']}
        else:
            self.request.status_int = fcode
            rtn = {'data': status['data'], 'info': status['info']}
        return rtn

    def validate(self, schema, body=True):
        """
        Handle params sent from web requests
        """
        try:
            #log.debug('request param: %s' % self.request.params)
            #log.debug('request body: %s'  % self.request.body)
            target_dict = dict()
            to_check_dict = dict(self.request.params.copy())
            token = to_check_dict.pop('token', None)
            authn_userid = authenticated_userid(self.request)
            #log.debug('authn_userid pop out???: %s' % authn_userid)
            if authn_userid:
                to_check_dict['userid'] = authn_userid[0]

            if body == True:
                target_dict.update(to_check_dict)
                if len(self.request.body) > 0:
                    target_dict.update(dict(self.request.json_body.copy()))
            else:
                target_dict.update(to_check_dict)

            data = dict(target_dict)
            data = schema.to_python(data)
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


