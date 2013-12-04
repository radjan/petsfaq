#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
__author__= 'samuel'

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
        super(location_tb, self).__init__(*args, **kwargs)

    @classmethod
    def create(cls, name, description, gps, address, userid):
        global DBSession
        try:
            model = cls(name=name, description=desc, gps=gps, 
                        address=addr, userid=userid,)
            DBSession.add(model)
            DBSession.flush()
            rtn = (True, model)
        except Exception, e:
            import traceback
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
