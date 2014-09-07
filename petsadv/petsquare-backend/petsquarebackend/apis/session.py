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
#from pyramid.security import authenticated_userid
from pyramid.security import remember 
from pyramid.security import forget

from petsquarebackend.apis import BaseAPI

#from petsquarebackend.services.account import AccountService
#FIXME
#directly using User_TB with DBSession temporarily
from petsquarebackend.models.accounts import User_TB
from petsquarebackend.models import DBSession

class Schema_login_post(Schema):
    name        = validators.UnicodeString()
    password    = validators.UnicodeString()

@view_defaults(renderer='json')
class LoginAPI(BaseAPI):
    @view_config(route_name='weblogin', request_method='POST')
    def login(self):
        headers = remember(self.request, 1)
        self.request.response.headerlist.extend(headers)
        return {'status':'under construction', 'route_name': 'weblogin'}

    @view_config(route_name='weblogin', request_method='DELETE', permission='login')
    def logout(self):
        headers = forget(self.request)
        self.request.response.headerlist.extend(headers)
        return {'status':'under construction', 'route_name': 'weblogout'}


def main():
    pass

if __name__ == '__main__':
    main()

