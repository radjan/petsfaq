#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
__author__= 'samuel'

import logging
log = logging.getLogger(__name__)

import inspect
import traceback

from petsquarebackend import common
from petsquarebackend.common import util

def ServiceMethod(func):
    def serv_wrapped(self, *args, **kwargs):
        try:
            status = func(self, *args, **kwargs)
        except Exception, e:
            status = util.return_dict(success=False,
                                      code=common.DEFAULT_ERROR_CODE)
            self.serv_exception_rtn(
                    status=status, 
                    exp=e, 
                    ins_stk=inspect.stack()[0][3],
                    tbk=traceback.format_exc())
        return status
    return serv_wrapped
     
class BaseService(object):

    def __init__(self, service_cls, request=None):
        self.service_cls = service_cls
        self.request = request

    #@classmethod
    def serv_exception_rtn(self, status, exp, ins_stk, tbk):
        status = self._default_status(False, status, None, status['code'])
        err_info = (self.service_cls, ins_stk, tbk)
        log.error('%s:%s, traceback:\n %s' % err_info)
        status['data'] = ''
        status['success'] = False
        status['info'] = {'status':'fail',
                          'msg':'DB internal error on %s, %s, %s' % err_info}
        return status

    @classmethod
    def serv_rtn(cls, status=None, success=False, model=None, code=None):
        # TODO rename
        data = model
        status = cls._default_status(success, status, data, code)
        status['data'] = data if success else ''
        status['info'] = {'status': success,
                          'msg': '' if success else data}
        return status

    @classmethod
    def _default_status(cls, success, status, data, code):
        # give default values
        if success and code is None:
            code = common.DEFAULT_SUCCESS_CODE
        elif code is None:
            code = common.ERROR_CODE_MAPPING.get(data,
                                                 common.DEFAULT_ERROR_CODE)
        if status is None:
            status = util.return_dict(success=success,
                                      data='',
                                      info='',
                                      code=code)
        else:
            status['code'] = code
        return status


def main():
    pass

if __name__ == '__main__':
    main()
