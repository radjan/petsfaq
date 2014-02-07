#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 07, 2014 '
__author__= 'samuel'

from zope.interface import implementer

from pyramid.interfaces import IAuthenticationPolicy
from pyramid.security import Everyone, Authenticated
from pyramid.authentication import CallbackAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.util import DottedNameResolver


@implementer(IAuthenticationPolicy)
class TokenAuthenticationPolicy(CallbackAuthenticationPolicy):
    def unauthenticated_userid(self, request):
        return 1
    def unauthenticated_userid(self, request):
        return 1
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
