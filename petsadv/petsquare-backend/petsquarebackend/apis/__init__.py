#!/usr/bin/env python                                                 
# -*- coding: utf-8 -*- 

import logging
log = logging.getLogger(__name__)

from formencode import Invalid

class BaseAPI(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def handle_serv_rtn(self, serv_rtn, fcode=500, scode=200):
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

    def handle_req_params(self, schema):
        """
        Handle params sent from web requests
        """
        try:
            target_dict = dict()
            target_dict.update(dict(self.request.params.copy()))
            if len(self.request.body) > 0:
                target_dict.update(dict(self.request.json_body.copy()))

            data = dict(self.request.params.copy())
            data = schema.to_python(data)
            rtn = (True, data, 200)

        except Invalid, e:
            errors = e.unpack_errors()
            rtn = (False, errors, 400)
        return rtn

