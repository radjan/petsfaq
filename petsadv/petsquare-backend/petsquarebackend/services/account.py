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
                new_user_id = acc_status['data'].id

                token_service = TokenService(self.request)
                token_status = token_service.create(new_user_id, authn_by=login_type, sso_info=sso_info)
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
    def sso_logout(self, token):
        status = self.status.copy()
        if not token:
            return status
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

    #@ServiceMethod
    #def fb_email_check(self, email):
    #    status = self.status.copy()
    #    service = TokenService(self.request)
    #    status = service.fb_email_validate(email)
    #    return status

    #@ServiceMethod
    #def twitter_acc_check(self, account):
    #    status = self.status.copy()
    #    service = TokenService(self.request)
    #    status = service.twitter_acc_validate(account)
    #    return status

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
    def show(self, id):
        status = self.status.copy()
        success, model = User_TB.show(id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status




def main():
    pass

if __name__ == '__main__':
    main()

