#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 13, 2014 '
__author__= 'samuel'

"""
APIs

    GET /app/v1/user/me (show user itself)
    'app-showme', AccountAPP.showme()

    PUT /app/v1/user/{id} (update user itself)
    'app-user', AccountAPP.user_update()
"""

import traceback
import json
import logging
log = logging.getLogger(__name__)

import formencode
from formencode import Schema
from formencode import validators

from pyramid.view import (
        view_config,
        view_defaults,
        )
from pyramid.security import authenticated_userid

from petsquarebackend.apis import BaseAPI
from petsquarebackend.apis import BaseAPP
from petsquarebackend.services.account import AccountService

class Schema_users_post(Schema):
    name        = validators.UnicodeString(if_missing=u'PlaceName')

class Schema_user_put(Schema):
    name        = validators.UnicodeString(if_missing=None)
    description = validators.UnicodeString(if_missing=None)
    password    = validators.UnicodeString(if_missing=None)
    email       = validators.UnicodeString(if_missing=None)
    fb_id       = validators.UnicodeString(if_missing=None)
    activated   = validators.Bool(if_missing=None)
    group_id    = validators.Int(if_missing=None)

class Schema_user_get(Schema):
    offset  = validators.Int(if_missing=0)
    size    = validators.Int(if_missing=100)


class BaseAccount(object):
    def _showme(self):
        success, data, code = self.validate(Schema_user_get)
        if success:
            serv = AccountService(self.request)
            serv_rtn = serv.show(data['user_id'])
                                 
        else:
            #mock fake serv_rtn
            serv_rtn = {'data':'', 
                        'info':data, 
                        'code':code, 
                        'success':False}

        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _user_update(self):
        #validation
        success, data, code = self.validate(Schema_user_put)

        log.debug('user updated after valided.')
        try:
            #get id from route_path
            userid = self.request.matchdict['id'].encode('utf-8', 'ignore')
        except Exception, e:
            success = False
        if success:
            serv = AccountService(self.request)
            serv_rtn = serv.update(id=userid, data=data)
            log.debug('updated return status: %s' % serv_rtn)
        else:
            log.debug('error: %s' % data)
            #mock fake serv_rtn
            serv_rtn = {'data':'',
                        'info':data,
                        'code':code,
                        'success':False,
                        }

        api_rtn = self.format_return(serv_rtn)
        return api_rtn


@view_defaults(renderer='json')
class AccountAPP(BaseAPP, BaseAccount):
    #@view_config(route_name='showme', request_method='GET', permission='login')
    @view_config(route_name='app-showme', request_method='GET', permission='login')
    def showme(self):
        return self._showme()

    #@view_config(route_name='user', request_method='PUT')
    @view_config(route_name='app-user', request_method='PUT')
    def user_update(self):
        return self._user_update()


def main():
    pass

if __name__ == '__main__':
    main()
