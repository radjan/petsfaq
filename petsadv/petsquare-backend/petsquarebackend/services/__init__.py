#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
__author__= 'samuel'

import logging
log = logging.getLogger(__name__)

import inspect
import traceback

def ServiceMethod(func):
    def serv_wrapped(self, *args, **kwargs):
        try:
            status = func(self, *args, **kwargs)
        except Exception, e:
            status = self.status.copy()
            self.serv_exception_rtn(
                    status=status, 
                    exp=e, 
                    ins_stk=inspect.stack()[0][3],
                    tbk=traceback.format_exc())
        return status
    return serv_wrapped
     
class BaseService(object):
    status = {'code':0,
              'success': False,
              'data': '',
              'info': ''}

    def __init__(self, service_cls, request=None):
        self.service_cls = service_cls
        self.request = request

    #@classmethod
    def serv_exception_rtn(self, status, exp, ins_stk, tbk):
        err_info = (self.service_cls, ins_stk, tbk)
        log.error('%s:%s, traceback:\n %s' % err_info)
        status['data'] = ''
        status['success'] = False
        status['info'] = {'status':'fail',
                          'msg':'DB internal error on %s, %s, %s' % err_info}
        return status

    @classmethod
    def new_status(cls):
        return cls.status.copy()

    @classmethod
    def serv_rtn(cls, status=None, success=False, model=None):
        if status is None:
            status = cls.new_status()
        status['data'] = model if success else ''
        status['success'] = success
        status['info'] = {'status':success, 
                          'msg':'' if success else model}
        return status





def main():
    pass

if __name__ == '__main__':
    main()
