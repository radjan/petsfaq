#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 07, 2014 '
__author__= 'samuel'

import logging
log = logging.getLogger(__name__)

from zope.interface import implementer

from pyramid.interfaces import IAuthenticationPolicy
from pyramid.security import Everyone, Authenticated
from pyramid.authentication import CallbackAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.util import DottedNameResolver

from petsquarebackend.services.accounts import AccountService

@implementer(IAuthenticationPolicy)
class TokenAuthenticationPolicy(CallbackAuthenticationPolicy):
    def unauthenticated_userid(self, request):
        return []
    def authenticated_userid(self, request):
        token = request.params.get('token', None)
        acc_service = AccountService(request)
        serv_rtn = acc_service.sso_check(token)
        rtn_list = []
        if serv_rtn['data']:
            rtn_list = [serv_rtn['data'].id]
        else:
            rtn_list = []
        return rtn_list
    def effective_principals(self, request):
        return [Everyone]
    def remember(self, request, principal, **wk):
        return []
    def forget(self, request):
        return []

def main():
    pass

if __name__ == '__main__':
    main()
