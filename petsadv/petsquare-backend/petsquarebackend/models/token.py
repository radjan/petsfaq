#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 08, 2014 '
__author__= 'samuel'

import logging
log = logging.getLogger(__name__)

from petsquarebackend.models import DBSession
from petsquarebackend.models import Base, MODEL_DEFAULT_DEPTH, tmpObj
from petsquarebackend.models import ModelMethod

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

from sqlalchemy.types import (
        BigInteger,
        Integer,
        String,
        Boolean,
        DateTime,
        UnicodeText,
        Float,
        )

import datetime
import traceback
import json

class Token_TB(Base):
    __tablename__ = 'token'
    __public__ = ('id','token', 'authn_by', 'sso_info',
            'user_id',  #fk
            'user',     #backref
            'createddatetime', 'updateddatetime')

    id       = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    token    = Column(String(255), nullable=True, unique=False,)
    authn_by = Column(String(255), nullable=True, unique=False,)
    sso_info = Column(UnicodeText(255),  nullable=True, unique=False,)
    #fk
    user_id  = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)
    #relation
    updateddatetime = Column(DateTime, nullable=False)
    createddatetime = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Token_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, user_id, token=None, authn_by=None, sso_info=None):
        global DBSession
        model = cls(token=token, authn_by=authn_by, sso_info=json.dumps(sso_info), user_id=user_id)
        DBSession.add(model)
        DBSession.flush()
        rtn_model = tmpObj()
        rtn_model.update = cls.update
        rtn_model.id              = model.id
        rtn_model.token           = model.token
        rtn_model.authn_by        = model.authn_by
        rtn_model.sso_info        = json.loads(model.sso_info)
        rtn_model.updateddatetime = model.updateddatetime
        rtn_model.createddatetime = model.createddatetime
        rtn_model.user = model.user
        rtn = (True, rtn_model)
        return rtn

    @classmethod
    @ModelMethod
    def list(cls, filattr=None, offset=None, size=None):
        """
        return type: dict-list(list contains dict)
        """
        model_list = cls.get_all(filattr=filattr, offset=offset, limit=size)
        rtn_list = []
        for model in model_list:
            rtn_model = tmpObj()
            rtn_model.update = cls.update
            rtn_model.id              = model.id
            rtn_model.token           = model.token
            rtn_model.authn_by        = model.authn_by
            rtn_model.sso_info        = json.loads(model.sso_info)
            rtn_model.updateddatetime = model.updateddatetime
            rtn_model.createddatetime = model.createddatetime
            rtn_model.user = model.user
            rtn_list.append(rtn_model)
        rtn = (True, rtn_list)
        return rtn

    @classmethod
    @ModelMethod
    def show(cls, id):
        """
        return type: dict
        """
        model = cls.get_by_id(id)
        rtn_model = tmpObj()
        rtn_model.update = cls.update
        rtn_model.id              = model.id
        rtn_model.token           = model.token
        rtn_model.authn_by        = model.authn_by
        rtn_model.sso_info        = json.loads(model.sso_info)
        rtn_model.updateddatetime = model.updateddatetime
        rtn_model.createddatetime = model.createddatetime
        rtn_model.user = model.user
        rtn = (True, rtn_model)
        return rtn

    @classmethod
    @ModelMethod
    def update(cls, id, token=None, authn_by=None, sso_info=None, user_id=None):
        """
        return type: dict
        """
        model = cls.get_by_id(id)
        updateddatetime = datetime.datetime.now()
        log.debug('model update: %s' % model)

        #FIXME
        if token:    model.token = token
        if authn_by: model.authn_by = authn_by
        if sso_info: model.sso_info = json.dumps(sso_info)
        if user_id:  model.user_id = user_id
        model.updateddatetime = updateddatetime
        DBSession.merge(model)

        rtn_model = tmpObj()
        rtn_model.update = cls.update
        rtn_model.id              = model.id
        rtn_model.token           = model.token
        rtn_model.authn_by        = model.authn_by
        rtn_model.sso_info        = json.loads(model.sso_info)
        rtn_model.updateddatetime = model.updateddatetime
        rtn_model.createddatetime = model.createddatetime
        rtn_model.user = model.user
        rtn = (True, rtn_model)
        return rtn

    @classmethod
    @ModelMethod
    def delete(cls, id):
        rtn = cls.delete_by_id(id)
        return rtn

    @ModelMethod
    def __json__(self, request, exclude=(), extra=(), exclude_fk=True,
            max_depth=MODEL_DEFAULT_DEPTH):
        super_rtn = super(Token_TB, self).__json__(request, exclude=exclude, 
                                                   extra=extra,
                                                   exclude_fk=exclude_fk,
                                                   max_depth=max_depth)
        super_rtn['sso_info'] = json.loads(super_rtn['sso_info'])
        return super_rtn

def main():
    pass

if __name__ == '__main__':
    main()
