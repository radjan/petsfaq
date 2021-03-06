#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 02, 2014 '
__author__= 'samuel'

import traceback
import json
import logging
log = logging.getLogger(__name__)

#import formencode
#from formencode import Schema
#from formencode import validators
#
from pyramid.view import (
        view_config,
        view_defaults,
        )

from petsquarebackend.apis import BaseAPI
from petsquarebackend.apis.login import BaseLogin
from petsquarebackend.services.account import AccountService

@view_defaults(renderer='json')
class SSO_API(BaseAPI, BaseLogin):
    @view_config(context='velruse.providers.facebook.FacebookAuthenticationComplete')
    def facebook_logged_in_cb(self):
        context = self.request.context
        p_name = context.provider_name
        if p_name == 'facebook_mobile':
            return self._facebook_logged_in_cb_mobile()
        else:
            return self._facebook_logged_in_cb_web()

    @view_config(route_name='app-ssologout-facebook', request_method='DELETE')
    def facebook_logged_out(self):
        return self._token_logout()

    @view_config(context='velruse.providers.twitter.TwitterAuthenticationComplete')
    def twitter_logged_in_cb(self):
        context = self.request.context
        result = {
                'provider_type': context.provider_type,
                'provider_name': context.provider_name,
                'profile':       context.profile,
                'credentials':   context.credentials,
                }
        #print result
        acc_service = AccountService(self.request)
        serv_rtn = acc_service.sso_login(login_type=context.provider_type,
                                         value=context.profile['accounts'][0]['username'],
                                         sso_info=result)
        api_rtn = self.format_return(serv_rtn)
        return api_rtn


@view_config(context='velruse.AuthenticationDenied', renderer='json')
def SSO_denied_cb(self):
    return {'info': {'status': 'access denied'},
            'data': None}


def main():
    pass

if __name__ == '__main__':
    main()
