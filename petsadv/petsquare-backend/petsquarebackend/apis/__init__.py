#!/usr/bin/env python                                                 
# -*- coding: utf-8 -*- 

import logging
log = logging.getLogger(__name__)

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

