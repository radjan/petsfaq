#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 08, 2014 '
__author__= 'samuel'

import logging
log = logging.getLogger(__name__)

import inspect
import traceback

from pyramid.security import authenticated_userid

from petsquarebackend.services import BaseService
from petsquarebackend.services import ServiceMethod
from petsquarebackend.services.token import TokenService
from petsquarebackend.models.token import Token_TB
from petsquarebackend.models.accounts import User_TB, Group_TB

class AccountService(BaseService):
    def __init__(self, request):
        super(AccountService, self).__init__('AccountService', request)

    @ServiceMethod
    def sso_login(self, login_type, value, sso_info={}):
        """
        type: token/facebook/twitter
        """
        status = self.status.copy()
        rtn_status= self.status.copy()

        if login_type == 'facebook':
            fb_name  = sso_info['profile']['preferredUsername']
            fb_email = sso_info['profile']['verifiedEmail']
            fb_id    = ''
            for acc in sso_info['profile']['accounts']:
                if acc['domain'] == 'facebook.com':
                    fb_id = acc['userid']

            serv_rtn = self.search_user_by_email(fb_email)
            if serv_rtn['success'] and serv_rtn['data']:
                token_service = TokenService(self.request)
                token_status = token_service.create(serv_rtn['data'].id, authn_by=login_type, sso_info=sso_info)
            elif serv_rtn['success']:
                acc_status = self.web_create(name=fb_name, email=fb_email, fb_id=fb_id)
                exist_user_id = acc_status['data'].id

                token_service = TokenService(self.request)
                token_status = token_service.create(exist_user_id, authn_by=login_type, sso_info=sso_info)
            else:
                token_status = self.status.copy()
                token_status['info']['msg'] = 'create token fail.'

            #return token from token
            rtn_status = token_status
            rtn_status['data'] = token_status['data'].token

        else:
            rtn_status = status
        return rtn_status


    @ServiceMethod
    def fb_access_token_login(self, fb_id, fb_access_token, fb_username, fb_email):
        status = self.status.copy()
        token_service = TokenService(self.request)
        token_serv_rtn = token_service.fb_access_token_validate(fb_access_token)

        """
        check fb_access_token exists in token table
        """
        if token_serv_rtn['success'] and token_serv_rtn['data']:
            """
            1a. return token
            """
            status['info'] = {'msg':'access_token verified'}
            status['data'] = token_serv_rtn['data'].token
        elif token_serv_rtn['success']:
            """
            1b. find user via fb_id, and return token
            """
            fbjs_info = {'id':fb_id,
                         'access_token':fb_access_token,
                         'username':fb_username,
                         'email':fb_email}
            acc_serv_rtn = self.search_user_by_fb_id(fb_id)
            if acc_serv_rtn['success'] and acc_serv_rtn['data']:
                #exist user
                exist_user_id = acc_serv_rtn['data'].id
                token_status = token_service.create(user_id=exist_user_id, 
                                                    authn_by='facebook_js', 
                                                    sso_info=fbjs_info)
                status['info'] = {'msg': 'token created'}
                status['data'] = token_status['data'].token
            elif acc_serv_rtn['success']:
                #create new user
                new_acc_status = self.web_create(name=fb_username, fb_id=fb_id)
                new_user_id = new_acc_status['data'].id
                token_status = token_service.create(user_id=new_user_id, 
                                                    authn_by='facebook_js', 
                                                    sso_info=fbjs_info)
                status['info'] = {'msg': 'token created'}
                status['data'] = token_status['data'].token
            else:
                status = self.status.copy()
                status['info']['msg'] = 'user not exist, create user fail.'
        else:
            status = self.status.copy()
            status['info']= {'msg': 'user not exist, create token fail.'}
        return status


    @ServiceMethod
    def token_logout(self, token):
        status = self.status.copy()
        if not token:
            return status
        service = TokenService(self.request)
        success, delete_msg = service.delete_by_token(token)
        if success:
            delete_msg['info'] = {'msg': 'logout'}
            return delete_msg
        else:
            return status

    @ServiceMethod
    def sso_check(self, token):
        status = self.status.copy()
        service = TokenService(self.request)
        status = service.token_validate(token)
        return status

    @ServiceMethod
    def web_create(self, name, description=None, password=None, email=None,
                   fb_id=None, activated=False, group_id=1):
        status = self.status.copy()
        success, model = User_TB.create(name=name, description=description,
                                        password=password,email=email,
                                        fb_id=fb_id, activated=activated,
                                        group_id=group_id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def search_user_by_email(self, email):
        status = self.status.copy()
        attr = ('email', email)
        success, model_list = User_TB.list(filattr=attr)
        hit_data = [m for m in model_list if (email == m.email)]
        result = hit_data[0] if len(hit_data) > 0 else None

        status = self.serv_rtn(status=status, success=success, model=result)
        return status

    @ServiceMethod
    def search_user_by_fb_id(self, fb_id):
        status = self.status.copy()
        attr = ('fb_id', fb_id)
        success, model_list = User_TB.list(filattr=attr)
        hit_data = [m for m in model_list if (fb_id == m.fb_id)]
        result = hit_data[0] if len(hit_data) > 0 else None

        status = self.serv_rtn(status=status, success=success, model=result)
        return status

    @ServiceMethod
    def show(self, id):
        status = self.status.copy()
        success, model = User_TB.show(id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def update(self, id, data):
        status = self.status.copy()
        name        = data.get('name', None)
        description = data.get('description', None)
        password    = data.get('password', None)
        email       = data.get('email', None)
        fb_id       = data.get('fb_id', None)
        activated   = data.get('activated', None)
        group_id    = data.get('group_id', None)

        success, model = User_TB.update(id=id,
                                        name=name,
                                        description=description,
                                        password=password,
                                        email=email,
                                        fb_id=fb_id,
                                        activated=activated,
                                        group_id=group_id)

        status = self.serv_rtn(status=status, success=success, model=model)
        return status

def main():
    pass

if __name__ == '__main__':
    main()

