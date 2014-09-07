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

from petsquarebackend.services.account import AccountService
import inspect
import traceback
import json

@implementer(IAuthenticationPolicy)
class TokenAuthenticationPolicy(CallbackAuthenticationPolicy):
    def unauthenticated_userid(self, request):
        """
        Actually, unauthenticated_userid() has no meaning to
        TokenAuthenticatedPolicy, just return None
        """
        return None

    def authenticated_userid(self, request):
        """
        using token value to query database
        """
        token = request.params.get('token', None)
        if not token:
            return None
        from petsquarebackend.models.token import Token_TB
        from petsquarebackend.models import DBSession

        try:
            model = DBSession.query(Token_TB).filter(Token_TB.token == token)\
                    .scalar()
            return None if model == None else model.user.id
        except Exception, e:
            err_msg = 'get authenticated_userid fail: %s' % json.dumps(
                        [str(e), inspect.stack()[0][3],
                         traceback.format_exc()], 
                        indent=1)
            log.error(err_msg)
            return None

    def effective_principals(self, request):
        principals = [Everyone]

        token = request.params.get('token', None)
        if not token:
            return principals
        from petsquarebackend.models.token import Token_TB
        from petsquarebackend.models import DBSession

        try:
            model = DBSession.query(Token_TB).filter(Token_TB.token == token)\
                    .scalar()
            if model == None:
                return principals
            else:
                principals += [Authenticated, 'u:%s' % model.user.id,
                               'g:%s' % model.user.group.name]
                return principals
        except Exception, e:
            err_msg = 'get effective_principals fail: %s' % json.dumps(
                        [str(e), inspect.stack()[0][3],
                         traceback.format_exc()], 
                        indent=1)
            log.error(err_msg)
            return [Everyone]

    def remember(self, request, principal, **wk):
        return []

    def forget(self, request):
        return []


def get_app_user(request):
    from petsquarebackend.models.token import Token_TB
    from petsquarebackend.models import DBSession

    try:
        model = DBSession.query(Token_TB).filter(Token_TB.token == token)\
                .scalar()
        return None if model == None else model.user
    except Exception, e:
        err_msg = 'get user obj fail: %s' % json.dumps(
                    [str(e), inspect.stack()[0][3],
                     traceback.format_exc()], 
                    indent=1)
        log.error(err_msg)
        return None

def main():
    pass

if __name__ == '__main__':
    main()

