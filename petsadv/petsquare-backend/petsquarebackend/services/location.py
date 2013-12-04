#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
__author__= 'samuel'

import traceback
import logging
log = logging.getLogger(__name__)
import inspect

from petsquarebackend.services import BaseService
from petsquarebackend.models.location import Location_TB

class LocationService(BaseService):
    def __init__(self, request):
        super(LocationService, self).__init__('LocationService', request)

    def list(self, userid=None, offset=0, size=100):
        status = self.status.copy()
        try:
            if userid:
                models = Location_TB.list(filattr=('userid', userid),
                                          offset=offset,
                                          size=size)
            else:
                models = Location_TB.list(offset=offset,
                                          size=size)

            status['data'] = models
            status['success'] = True
            status['info'] = {'status':'done', 'msg':'', 'count':len(models)}

        except Exception, e:
            err_info = (self.service_cls, inspect.stack()[0][3], traceback.format_exc())
            log.debug('%s:%s, traceback:\n %s' % err_info)
            status['data'] = ''
            status['success'] = False
            status['info'] = {'status':'fail', 'msg':err_info}

        return status


    def create(self):
        status = self.status.copy()
        try:
            #####################
            # method logic here!!
            #
            # >> @#!@#$!@#$!@$!@$
            #
            #####################
            status['data'] = 'I\'ve done.'
            status['success'] = True
            status['info'] = {'status':'done', 'msg':'I\'ve done.'}
        except Exception, e:
            log.debug('%s:%s, traceback:\n %s' % 
                        (self.service_cls, 
                         inspect.stack()[0][3]),
                         traceback.format_exc())
            status['data'] = 'I failed.'
            status['success'] = False
            status['info'] = {'status':'fail', 'msg':'I failed.'}
        return status


    def show(self, id):
        status = self.status.copy()
        try:
            model = Location_TB.show(id)
            status['data'] = model
            status['success'] = True
            status['info'] = {'status':'done', 'msg':''}

        except Exception, e:
            err_info = (self.service_cls, inspect.stack()[0][3], traceback.format_exc())
            log.debug('%s:%s, traceback:\n %s' % err_info)
            status['data'] = ''
            status['success'] = False
            status['info'] = {'status':'fail', 'msg':err_info}

        return status


    def update(self, id):
        status = self.status.copy()
        try:
            #####################
            # method logic here!!
            #
            # >> @#!@#$!@#$!@$!@$
            #
            #####################
            status['data'] = 'I\'ve done.'
            status['success'] = True
            status['info'] = {'status':'done', 'msg':'I\'ve done.'}
        except Exception, e:
            log.debug('%s:%s, traceback:\n %s' % 
                        (self.service_cls, 
                         inspect.stack()[0][3]),
                         traceback.format_exc())
            status['data'] = 'I failed.'
            status['success'] = False
            status['info'] = {'status':'fail', 'msg':'I failed.'}
        return status


    def delete(self, id):
        status = self.status.copy()
        try:
            #####################
            # method logic here!!
            #
            # >> @#!@#$!@#$!@$!@$
            #
            #####################
            status['data'] = 'I\'ve done.'
            status['success'] = True
            status['info'] = {'status':'done', 'msg':'I\'ve done.'}
        except Exception, e:
            log.debug('%s:%s, traceback:\n %s' % 
                        (self.service_cls, 
                         inspect.stack()[0][3]),
                         traceback.format_exc())
            status['data'] = 'I failed.'
            status['success'] = False
            status['info'] = {'status':'fail', 'msg':'I failed.'}
        return status


def main():
    pass

if __name__ == '__main__':
    main()
