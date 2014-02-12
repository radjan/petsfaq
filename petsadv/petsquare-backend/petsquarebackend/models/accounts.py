#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Jan 07, 2014 '
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

class Group_TB(Base):
    __tablename__ = 'group'
    __public__ = ('id','name','description','users',
            'createddatetime', 'updateddatetime')

    id          = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name        = Column(String(255), nullable=True, unique=False)
    description = Column(String(255), nullable=True, unique=False)
    #image_id    = Column(Integer, ForeignKey('image.id'), nullable=True, unique=False)

    users       = relationship('User_TB', backref=backref('group', order_by=id))

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Group_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, name, description):
        global DBSession
        model = cls(name=name, description=description)
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
    def update(cls, name, description):
        model = cls.get_by_id(id)
        updateddatetime = datetime.datetime.now()
        log.debug('model update: %s' % model)

        #FIXME
        if name:        model.name = name
        if description: model.description = description
        model.updateddatetime = updateddatetime
        DBSession.merge(model)
        rtn =  (True, model)
        return rtn

    @classmethod
    @ModelMethod
    def delete(cls, id):
        rtn = cls.delete_by_id(id)
        return rtn



class User_TB(Base):
    __tablename__ = 'user'
    __public__ = ('id','name','description', 'password', 'email', 'activated',
            'group_id',                               #fk
            'group',                                  #backref
            'images', 'locations', 'checks', 'tokens',#relation
            'pets', 'found_animals',
            'createddatetime', 'updateddatetime')

    id            = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name          = Column(String(255), nullable=True, unique=False)
    description   = Column(String(255), nullable=True, unique=False)
    password      = Column(String(255), nullable=True, unique=False)
    email         = Column(String(255), nullable=True, unique=False)
    activated     = Column(Boolean,     nullable=True, unique=False)

    group_id      = Column(Integer, ForeignKey('group.id'), nullable=False, unique=False)

    images        = relationship('Image_TB',    backref=backref('uploader', order_by=id))
    locations     = relationship('Location_TB', backref=backref('explorer', order_by=id))
    checks        = relationship('Check_TB',    backref=backref('user', order_by=id))
    tokens        = relationship('Token_TB',    backref=backref('user', order_by=id))

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    pets = relationship('Animal_TB', backref=backref('owner', order_by=id),
                        foreign_keys='[Animal_TB.owner_id]')
    found_animals = relationship('Animal_TB', backref=backref('finder', order_by=id),
                        foreign_keys='[Animal_TB.finder_id]')

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(User_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, name, description, password, email, activated, group_id):
        global DBSession
        model = cls(name=name, description=description, password=password, 
                email=email, activated=activated, group_id=group_id)
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
    def update(cls, name, description, password, email, activated, group_id):
        model = cls.get_by_id(id)
        updateddatetime = datetime.datetime.now()
        log.debug('model update: %s' % model)

        #FIXME
        if name:        model.name        = name
        if description: model.description = description
        if password:    model.password    = password
        if email:       model.email       = email
        if activated:   model.activated   = activated
        if group_id:    model.group_id    = group_id
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
