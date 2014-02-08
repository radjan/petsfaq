#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 08, 2014 '
__author__= 'samuel'

import logging
log = logging.getLogger(__name__)

import inspect
import traceback

from petsquarebackend.services import BaseService
from petsquarebackend.services import ServiceMethod
from petsquarebackend.models.token import Token_TB

from cryptacular.bcrypt import BCRYPTPasswordManager
import hashlib
import random
import string

class TokenService(BaseService):
    def __init__(self, request):
        super(TokenService, self).__init__('TokenService', request)

    @ServiceMethod
    def list(self, user_id=None, offset=0, size=100):
        status = self.status.copy()
        if user_id:
            success, models = Token_TB.list(filattr=('explorer_id', user_id),
                                      offset=offset,
                                      size=size)
        else:
            success, models = Token_TB.list(offset=offset,
                                      size=size)

        status = self.serv_rtn(status=status, success=success, model=models)
        status['info']['count'] = len(models)
        return status

    @ServiceMethod
    def create(self, user_id, authn_by=None, sso_info=None):
        status = self.status.copy()
        token=self._create_token(24)
        success, model = Token_TB.create(token=token, 
                                         authn_by=authn_by,
                                         sso_info=sso_info,
                                         user_id=user_id)
        status = self.serv_rtn(status=status, success=success, model=token)
        return status

    @ServiceMethod
    def show(self, id):
        status = self.status.copy()
        success, model = Token_TB.show(id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def token_validate(self, token):
        status = self.status.copy()
        model = Token_TB.get_by_attr(attr='token', value=token)
        status = self.serv_rtn(status=status, success=True, model=model)
        if status['data']:
            model.update(model.id)
            status['data'] = model.user
        return status

    @ServiceMethod
    def fb_email_validate(self, email):
        status = self.status.copy()
        attrs = [('authn_by', 'facebook')]
        success, model_list = Token_TB.get_by_attrs(attrs=attrs)

        hit_data = [m for m in model_list if (email in m.sso_info)]
        result = hit_data[0] if len(hit_data) > 0 else None

        status = self.serv_rtn(status=status, success=success, model=result)
        if result:
            result.update(result.id)
            status['data'] = result.user
        return status

    @ServiceMethod
    def twitter_acc_validate(self, account):
        log.debug('twitter account validation, acc: %s' % account)
        status = self.status.copy()
        attrs = [('authn_by', 'twitter')]
        success, model_list = Token_TB.get_by_attrs(attrs=attrs)

        hit_data = [m for m in model_list if (account in m.sso_info)]
        result = hit_data[0] if len(hit_data) > 0 else None

        status = self.serv_rtn(status=status, success=success, model=result)
        if result:
            result.update(result.id)
            status['data'] = result.user
        return status


    @ServiceMethod
    def update(self, id, data):
        status = self.status.copy()
        success, model = Token_TB.update(id=id,
                           name=data['name'],
                           description=data['description'],
                           longtitude=data['longtitude'],
                           latitude=data['latitude'],
                           address=data['address'],
                           explorer_id=data['user_id'],)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def delete(self, id):
        status = self.status.copy()
        success, model = Token_TB.delete(id=id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def delete_by_token(self, token):
        status = self.status.copy()
        model = Token_TB.get_by_attr(attr='token', value=token)
        status = self.serv_rtn(status=status, success=True, model=model)
        if status['data']:
            success, model = model.delete(id=model.id)
            status = self.serv_rtn(status=status, success=True, model=model)
        return status

    @ServiceMethod
    def _create_token(self, length):
        m = hashlib.sha512()
        word = ''
        for i in xrange(length):
            word += random.choice(string.ascii_letters)
        m.update(word)
        return unicode(m.hexdigest()[:length])


def main():
    pass

if __name__ == '__main__':
    main()
