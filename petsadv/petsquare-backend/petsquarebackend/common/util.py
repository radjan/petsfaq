#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Fan 23, 2014 '
__author__= 'rad'
import logging
log = logging.getLogger(__name__)

def return_dict(success=False, data='', info='', code=200):
    return {'data': data,
            'info': info,
            'code': code,
            'success':success}




def return_tmpObj():
    class tmpObj:
        pass
    return tmpObj()

