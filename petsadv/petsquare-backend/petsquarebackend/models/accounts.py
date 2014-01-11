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

    users       = relationship('User_TB', backref=backref('user.group_id', order_by=id))

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Group_TB, self).__init__(*args, **kwargs)


class User_TB(Base):
    __tablename__ = 'user'
    __public__ = ('id','name','description',
            'password',
            'fb_api_key','fb_api_secret', 
            'group_id', 'group',
            'images', 'checks',
            'createddatetime', 'updateddatetime')

    id            = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name          = Column(String(255), nullable=True, unique=False)
    description   = Column(String(255), nullable=True, unique=False)
    password      = Column(String(255), nullable=True, unique=False)
    fb_api_key    = Column(String(255), nullable=True, unique=False)
    fb_api_secret = Column(String(255), nullable=True, unique=False)

    group_id      = Column(Integer, ForeignKey('group.id'), nullable=False, unique=False)
    group         = relationship('Group_TB', backref=backref('user.group_id', order_by=id))

    images        = relationship('Image_TB', backref=backref('image.userid', order_by=id))
    checks        = relationship('Check_TB', backref=backref('image.userid', order_by=id))

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(User_TB, self).__init__(*args, **kwargs)

def main():
    pass

if __name__ == '__main__':
    main()
