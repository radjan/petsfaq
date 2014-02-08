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
        type_to_method = {'token':    self.sso_check,
                          'facebook': self.fb_email_check,
                          'twitter':  self.twitter_acc_check}

        f = type_to_method.get(login_type, None)
        if f:
            status = f(value)

        if (status['success']) and (status['data'] == None):
            acc_status = self.web_create(name='')
            new_user_id = acc_status['data'].id

            token_service = TokenService(self.request)
            token_status = token_service.create(new_user_id, authn_by=login_type, sso_info=sso_info)

            #return token from token
            rtn_status = token_status
            rtn_status['data'] = token_status['data'].token

        elif (status['success']) and (status['data'] != None):
            #return token from user.tokens[0]
            rtn_status = status
            rtn_status['data'] = status['data'].tokens[0].token
        else:
            rtn_status = status
        return rtn_status

    @ServiceMethod
    def sso_logout(self, token):
        status = self.status.copy()
        service = TokenService(self.request)
        status = service.delete_by_token(token)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def sso_check(self, token):
        status = self.status.copy()
        service = TokenService(self.request)
        status = service.token_validate(token)
        return status

    @ServiceMethod
    def fb_email_check(self, email):
        status = self.status.copy()
        service = TokenService(self.request)
        status = service.fb_email_validate(email)
        return status

    @ServiceMethod
    def twitter_acc_check(self, account):
        status = self.status.copy()
        service = TokenService(self.request)
        status = service.twitter_acc_validate(account)
        return status

    @ServiceMethod
    def web_create(self, name, description=None, password=None, 
                   activated=False, group_id=1):
        status = self.status.copy()
        success, model = User_TB.create(name=name, description=description,
                                        password=password,activated=activated, 
                                        group_id=group_id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status





def main():
    pass

if __name__ == '__main__':
    main()
