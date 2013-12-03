#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
__author__= 'samuel'

import traceback
import logging
log = logging.getLogger(__name__)

from petsquarebackend.services import BaseService

class LocationService(BaseService):
    def __init__(self, request):
        super(LocationService, self).__init__('LocationService', request)

    def list(self):
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
            import inspect
            log.debug('%s:%s, traceback:\n %s' % 
                        (self.service_cls, 
                         inspect.stack()[0][3]),
                         traceback.format_exc())
            status['data'] = 'I failed.'
            status['success'] = False
            status['info'] = {'status':'fail', 'msg':'I failed.'}
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
            import inspect
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
            import inspect
            log.debug('%s:%s, traceback:\n %s' % 
                        (self.service_cls, 
                         inspect.stack()[0][3]),
                         traceback.format_exc())
            status['data'] = 'I failed.'
            status['success'] = False
            status['info'] = {'status':'fail', 'msg':'I failed.'}
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
            import inspect
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
            import inspect
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
