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

@view_defaults(renderer='json')
class SSO_API(BaseAPI):
    @view_config(context='velruse.providers.twitter.TwitterAuthenticationComplete')
    def twitter_logged_in_cb(self):
        context = self.request.context
        result = {
                'provider_type': context.provider_type,
                'provider_name': context.provider_name,
                'profile':       context.profile,
                'credentials':   context.credentials,
                }
        return result

    @view_config(context='velruse.providers.facebook.FacebookAuthenticationComplete')
    def sso_cb(self):
        context = self.request.context
        result = {
                'provider_type': context.provider_type,
                'provider_name': context.provider_name,
                'profile':       context.profile,
                'credentials':   context.credentials,
                }
        return result


@view_config(context='velruse.AuthenticationDenied', renderer='json')
def SSO_denied_cb(self):
    return {'result': 'denied'}


def main():
    pass

if __name__ == '__main__':
    main()
