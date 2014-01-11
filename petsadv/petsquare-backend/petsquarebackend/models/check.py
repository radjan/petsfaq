#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 26, 2013 '
__author__= 'samuel'
import logging
log = logging.getLogger(__name__)

from petsquarebackend.models import DBSession
from petsquarebackend.models import Base
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

class Check_TB(Base):
    __tablename__  = 'check'

    id              = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    title           = Column(String(255), nullable=True, unique=False)
    description     = Column(String(255), nullable=True, unique=False)

    location_id     = Column(Integer, ForeignKey('location.id'), nullable=False, unique=False)
    image_id        = Column(Integer, ForeignKey('image.id'), nullable=False, unique=False)
    #userid          = Column(Integer, nullable=True, unique=False,)
    userid          = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)

    user = relationship('User_TB', backref=backref('userid', order_by=id))

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Check_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, title, description, location_id, image_id, userid):
        global DBSession
        model = cls(title=title, description=description,
                    location_id=location_id, image_id=image_id, 
                    userid=userid)
        DBSession.add(model)
        DBSession.flush()
        rtn = (True, model)
        return rtn

    @classmethod
    @ModelMethod
    def list(cls, filattr=None, offset=None, size=None):
        model_list = cls.get_all(filattr=filattr, offset=offset, limit=size)
        rtn = (True, model_list)
        return rtn

    @classmethod
    @ModelMethod
    def show(cls, id):
        model = cls.get_by_id(id)
        rtn = (True, model)
        return rtn

    @classmethod
    @ModelMethod
    def update(cls, id, title=None, description=None, location_id=None, image_id=None, userid=None):
        model = cls.get_by_id(id)
        updateddatetime = datetime.datetime.now()
        log.debug('model update: %s' % model)

        #FIXME
        if title:        model.title = title
        if description: model.description = description
        if location_id:  model.location_id = location_id
        if image_id:    model.image_id = image_id
        if address:     model.address = address
        if userid:      model.userid = userid
        model.updateddatetime = updateddatetime
        DBSession.merge(model)
        rtn =  (True, model)
        return rtn

    @classmethod
    @ModelMethod
    def delete(cls, id):
        rtn = cls.delete_by_id(id)
        return rtn

def main():
    pass

if __name__ == '__main__':
    main()

