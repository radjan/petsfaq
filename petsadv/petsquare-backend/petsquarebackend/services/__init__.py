#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
__author__= 'samuel'

class BaseService(object):
    def __init__(self, service_cls, request=None):
        self.service_cls = service_cls
        self.request = request
        self.status = {'code':0,
                       'success': False,
                       'data': '',
                       'info': ''}

def main():
    pass

if __name__ == '__main__':
    main()
