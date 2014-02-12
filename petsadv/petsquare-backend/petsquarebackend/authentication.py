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
        return None

    def authenticated_userid(self, request):
        if request.app_user:
            return request.app_user.id
        else:
            return None

    def effective_principals(self, request):
        principals = [Everyone]
        app_user = request.app_user
        if app_user:
            principals += [Authenticated, 'u:%s' % app_user.id]
            principals.extend(('g:%s' % g.name for g in app_user.group))
        return principals

    def remember(self, request, principal, **wk):
        return []

    def forget(self, request):
        return []


def get_app_user(request):
    try:
        token = request.params.get('token', None)
        if not token:
            return None
        acc_service = AccountService(request)
        serv_rtn = acc_service.sso_check(token)

        if serv_rtn['success']:
            return serv_rtn['data']
        else:
            return None
    except Exception, e:
        log.error('error: %s' % str(e))
        return None


def main():
    pass

if __name__ == '__main__':
    main()


