#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 15, 2014 '
__author__= 'samuel'

import requests
import json

import logging
log = logging.getLogger(__name__)

import inspect
import traceback

from pyramid.view import (
        view_config,
        view_defaults,
        )

from petsquarebackend.apis import BaseAPI
from petsquarebackend.apis import BaseAPP
from petsquarebackend.services.account import AccountService
from petsquarebackend.services.token import TokenService

class BaseLogin(object):
    def _facebook_logged_in_cb_mobile(self):
        context = self.request.context
        result = {
                'provider_type': context.provider_type,
                'provider_name': context.provider_name,
                'profile':       context.profile,
                'credentials':   context.credentials,
                }
        #result = {'verifiedEmail': context.profile['verifiedEmail'],
        #          'credentials':   context.credentials,
        #          'provider_type': context.provider_type,
        #          }
        acc_service = AccountService(self.request)
        serv_rtn = acc_service.sso_login(login_type=context.provider_type,
                                         value=context.profile['verifiedEmail'],
                                         sso_info=result)
        api_rtn = self.format_return(serv_rtn)
        return api_rtn

    def _facebook_logged_in_cb_web(self):
        context = self.request.context
        result = {
                'provider_type': context.provider_type,
                'provider_name': context.provider_name,
                'profile':       context.profile,
                'credentials':   context.credentials,
                }
        return {'info': 'facebook sso web callback not ready yet.',
                'data': result}

    def _token_logout(self):
        acc_service = AccountService(self.request)
        serv_rtn = acc_service.token_logout(self.request.params.get('token', None))
        api_rtn = self.format_return(serv_rtn)
        return api_rtn


@view_defaults(renderer='json')
class LoginAPP(BaseAPP, BaseLogin):
    @view_config(route_name='app-login-facebook', request_method='POST')
    def facebook_login(self):
        fb_id = self.request.params.get('fb_id', None)
        fb_access_token = self.request.params.get('fb_access_token', None)

        success, fb_info = self._check_fb_verified(fb_id, fb_access_token)
        rtn = {}
        if success:
            acc_service = AccountService(self.request)
            serv_rtn = acc_service.fb_access_token_login(fb_id=fb_info['id'],
                                                         fb_access_token=fb_access_token,
                                                         fb_username=fb_info['username'])
            serv_rtn['data'] = {'token': serv_rtn['data']}
            api_rtn = self.format_return(serv_rtn)
        else:
            api_rtn =  {'info': {'status': 'access denied', 'msg': fb_info},
                        'data': None}
        return api_rtn

    @view_config(route_name='app-logout-facebook', request_method='DELETE')
    def facebook_logout(self):
        return self._token_logout()

    def _check_fb_verified(self, fb_id=None, fb_access_token=None):
        if (not fb_access_token) or (not fb_id):
            return (False, 'error: fb_id or fb_acceess_token is empty parameter.')
        try:
            validation_api_prefix = 'https://graph.facebook.com/me?fields=username,id,email&access_token='
            validation_api = validation_api_prefix + fb_access_token
            r = requests.get(validation_api)
            fb_info = json.loads(r.text)
            if fb_info['id'] == fb_id:
                rtn = (True, fb_info)
            else:
                rtn = (False, fb_info)
        except Exception,e:
            ins_stk=inspect.stack()[0][3]
            tbk=traceback.format_exc()
            exp=str(e)
            rtn = (False, '%s, %s, %s' % (exp, ins_stk, tbk))
        return rtn


def main():
    pass

if __name__ == '__main__':
    main()
