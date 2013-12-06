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
        )

import datetime
import traceback

class Location_TB(Base):
    __tablename__ = 'location'
    id              = Column(Integer(10), nullable=False, unique=True, 
                             primary_key=True, autoincrement=True)
    name            = Column(String(255), nullable=True, unique=False, )
    description     = Column(String(255), nullable=True, unique=False,)
    gps             = Column(String(255), nullable=True, unique=False,)
    address         = Column(String(255), nullable=True, unique=False,)
    userid          = Column(Integer(10), nullable=True, unique=False,)
    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Location_TB, self).__init__(*args, **kwargs)

    @classmethod
    def create(cls, name, description, gps, address, userid):
        global DBSession
        try:
            model = cls(name=name, description=description, gps=gps, 
                        address=address, userid=userid)
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
    def update(cls, id, name=None, description=None, gps=None, address=None, userid=None):
        model = cls.get_by_id(id)
        try:
            #FIXME
            if name:        model.name = name
            if description: model.description = description
            if gps:         model.gps = gps
            if address:     model.address = address
            if userid:      model.userid = userid
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
            rtn = (True, cls.delete_by_id(id))
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

