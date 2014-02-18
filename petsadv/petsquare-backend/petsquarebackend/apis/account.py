#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 13, 2014 '
__author__= 'samuel'

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
    #user_id     = validators.Int(if_missing=1)

class Schema_user_put(Schema):
    name        = validators.UnicodeString(if_missing=None)
    description = validators.UnicodeString(if_missing=None)
    password    = validators.UnicodeString(if_missing=None)
    email       = validators.UnicodeString(if_missing=None)
    fb_id       = validators.UnicodeString(if_missing=None)
    activated   = validators.Bool(if_missing=None)
    group_id    = validators.Int(if_missing=None)
    #user_id     = validators.Int(if_missing=1)

    
class Schema_user_get(Schema):
    offset  = validators.Int(if_missing=0)
    size    = validators.Int(if_missing=100)
    #user_id = validators.Int(if_missing=1)



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

#    """
#    For Inheritance Only
#    """
#    def _userss_list(self):
#        #validation
#        success, data, code = self.validate(Schema_users_get)
#
#        if success:
#            serv = AccountService(self.request)
#            serv_rtn = serv.list(user_id=data['user_id'], 
#                                 offset=data['offset'],
#                                 size=data['size'])
#        else:
#            #mock fake serv_rtn
#            serv_rtn = {'data':'', 
#                        'info':data, 
#                        'code':code, 
#                        'success':False}
#
#        api_rtn = self.format_return(serv_rtn)
#        return api_rtn
#
#    def _users_create(self):
#        #validation
#        success, data, code = self.validate(Schema_users_post)
#
#        if success:
#            serv = AccountService(self.request)
#            serv_rtn = serv.create(name=data['name'],
#                                   description=data['description'],
#                                   longtitude=data['longtitude'],
#                                   latitude=data['latitude'],
#                                   address=data['address'],
#                                   user_id=data['user_id'])
#        else:
#            #mock fake serv_rtn
#            serv_rtn = {'data':'', 
#                        'info':data, 
#                        'code':code, 
#                        'success':False}
#
#        api_rtn = self.format_return(serv_rtn)
#        return api_rtn
#
#    def _user_show(self):
#        #validation
#        success, data, code = self.validate(Schema_users_get)
#
#        try:
#            #get id from route_path
#            userid = self.request.matchdict['id'].encode('utf-8', 'ignore')
#        except Exception, e:
#            success = False
#
#        if success:
#            serv = AccountService(self.request)
#            serv_rtn = serv.show(id=userid)
#        else:
#            #mock fake serv_rtn
#            serv_rtn = {'data':'',
#                        'info':data,
#                        'code':code,
#                        'success':False,
#                        }
#
#        api_rtn = self.format_return(serv_rtn)
#        return api_rtn

#
#    def _user_delete(self):
#        #validation
#        success, data, code = self.validate(Schema_users_get)
#
#        try:
#            #get id from route_path
#            userid = self.request.matchdict['id'].encode('utf-8', 'ignore')
#        except Exception, e:
#            success = False
#
#        if success:
#            serv = AccountService(self.request)
#            serv_rtn = serv.delete(id=userid)
#        else:
#            #mock fake serv_rtn
#            serv_rtn = {'data':'',
#                        'info':data,
#                        'code':code,
#                        'success':False,
#                        }
#
#        api_rtn = self.format_return(serv_rtn)
#        return api_rtn


#@view_defaults(renderer='json')
#class AccountAPI(BaseAPI, BaseAccount):
#    @view_config(route_name='users', request_method='OPTIONS')
#    def users_option(self):
#        #self.XHeaders(methods=['POST'])
#        self.XHeaders(headers=['Content-Type','Accept'], methods=['POST'])
#        return {}
#
#    @view_config(route_name='user', request_method='OPTIONS')
#    def user_option(self):
#        #self.XHeaders(methods=['PUT','DELETE'])
#        self.XHeaders(headers=['Content-Type','Accept'], methods=['PUT','DELETE'])
#        return {}
#
#    @view_config(route_name='users', request_method='GET')
#    def accounts_list(self):
#        """
#        list users
#        API: GET /users
#        """
#        #for X-domain development
#        self.XHeaders()
#        return self._accounts_list()
#
#    #TODO: test me!
#    @view_config(route_name='users', request_method='POST')
#    def users_create(self):
#        """
#        create user
#        API: POST /users
#        """
#        #for X-domain development
#        self.XHeaders()
#        return self._users_create()
#
#    @view_config(route_name='user', request_method='GET')
#    def user_show(self):
#        """
#        show user
#        API: GET /user/<id:\d+>
#        """
#        #for X-domain development
#        self.XHeaders()
#        return self._user_show()
#
#    @view_config(route_name='user', request_method='PUT')
#    def user_update(self):
#        """
#        update users
#        API: PUT /user/<id:\d+>
#        """
#        #for X-domain development
#        self.XHeaders()
#        return self._user_update()
#
#
#    @view_config(route_name='user', request_method='DELETE')
#    def user_delete(self):
#        """
#        delete user
#        API: DELETE /user/<id:\d+>
#        """
#        #for X-domain development
#        self.XHeaders()
#        return self._user_delete()


@view_defaults(renderer='json')
class AccountAPP(BaseAPP, BaseAccount):
    @view_config(route_name='app-showme', request_method='GET', permission='login')
    def showme(self):
        return self._showme()

    #@view_config(route_name='app-users', request_method='GET')
    #def accounts_list(self):
    #    return self._accounts_list()

    #@view_config(route_name='app-users', request_method='POST')
    #def users_create(self):
    #    return self._users_create()

    #@view_config(route_name='app-user', request_method='GET', permission='login')
    #def user_show(self):
    #    return self._user_show()

    @view_config(route_name='app-user', request_method='PUT')
    def user_update(self):
        return self._user_update()

    #@view_config(route_name='app-user', request_method='DELETE')
    #def user_delete(self):
    #    return self._user_delete()


def main():
    pass

if __name__ == '__main__':
    main()
