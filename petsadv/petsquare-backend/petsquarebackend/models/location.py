#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
__author__= 'samuel'
import logging
log = logging.getLogger(__name__)

from petsquarebackend.models import DBSession
from petsquarebackend.models import Base

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

class Location_TB(Base):
    __tablename__ = 'location'
    id              = Column(Integer(10), nullable=False, unique=True, 
            primary_key=True, autoincrement=True)
    name            = Column(String(255), nullable=True, unique=False, )
    description     = Column(String(255), nullable=True, unique=False,)
    longtitude      = Column(Float(255), nullable=True, unique=False,)
    latitude        = Column(Float(255), nullable=True, unique=False,)
    address         = Column(String(255), nullable=True, unique=False,)
    userid          = Column(Integer(10), nullable=True, unique=False,)
    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Location_TB, self).__init__(*args, **kwargs)

    @classmethod
    def create(cls, name, description, longtitude, latitude, address, userid):
        global DBSession
        try:
            model = cls(name=name, description=description,
                    longtitude=longtitude, latitude=latitude, address=address, 
                    userid=userid)
            DBSession.add(model)
            DBSession.flush()
            rtn = (True, model)
        except Exception, e:
            err_tbk = traceback.format_exc()
            err_exp = str(e)
            #err_msg = err_exp + ', ' + err_tbk
            err_msg = err_exp
            log.debug(err_tbk)
            rtn = (False, '%s' % (err_msg))
        return rtn

    @classmethod
    def list(cls, filattr=None, offset=None, size=None):
        try:
            model_list = cls.get_all(filattr=filattr, offset=offset, limit=size)
            rtn = (True, model_list)
        except Exception, e:
            err_tbk = traceback.format_exc()
            err_exp = str(e)
            #err_msg = err_exp + ', ' + err_tbk
            err_msg = err_exp
            log.debug(err_tbk)
            rtn = (False, '%s' % (err_msg))
        return rtn


    @classmethod
    def show(cls, id):
        try:
            model = cls.get_by_id(id)
            rtn = (True, model)
        except Exception, e:
            err_tbk = traceback.format_exc()
            err_exp = str(e)
            #err_msg = err_exp + ', ' + err_tbk
            err_msg = err_exp
            log.debug(err_tbk)
            rtn = (False, '%s' % (err_msg))
        return rtn


    @classmethod
    def update(cls, id, name=None, description=None, longtitude=None,
            latitude=None, address=None, userid=None):
        model = cls.get_by_id(id)
        updateddatetime = datetime.datetime.now()
        log.debug('model update: %s' % model)
        try:
            #FIXME
            if name:        model.name = name
            if description: model.description = description
            if longtitude:  model.longtitude = longtitude
            if latitude:    model.latitude = latitude
            if address:     model.address = address
            if userid:      model.userid = userid
            model.updateddatetime = updateddatetime
            DBSession.merge(model)
            return (True, model)
        except Exception, e:
            err_tbk = traceback.format_exc()
            err_exp = str(e)
            #err_msg = err_exp + ', ' + err_tbk
            err_msg = err_exp
            log.debug(err_tbk)
            rtn = (False, '%s' % (err_msg))
        return rtn

    @classmethod
    def delete(cls, id):
        try:
            rtn = cls.delete_by_id(id)
        except Exception, e:
            err_tbk = traceback.format_exc()
            err_exp = str(e)
            #err_msg = err_exp + ', ' + err_tbk
            err_msg = err_exp
            log.debug(err_tbk)
            rtn = (False, '%s' % (err_msg))
        return rtn


def main():
    pass

if __name__ == '__main__':
    main()

