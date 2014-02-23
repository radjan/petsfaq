#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Jan 11, 2014 '
__author__= 'rad'
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
        BLOB,
        )

import datetime
import traceback
import Image as PILImage
import base64

class Animal_TB(Base):
    __tablename__ = 'animal'
    __public__ = ('id', 'name', 'type', 'sub_type', 'status', 'description',
                  'createddatetime', 'updateddatetime',
                  # foreign key
                  'finder_id', 'owner_id',
                  'find_location_id', 'current_location_id',
                  # relationship
                  'finder', 'owner', 'image_assocs')

    id              = Column(Integer, nullable=False, unique=True, 
                             primary_key=True, autoincrement=True)
    name            = Column(String(255), nullable=False, unique=False,)
    type            = Column(String(255), nullable=False, unique=False,)
    sub_type        = Column(String(255), nullable=False, unique=False,)
    status          = Column(String(255), nullable=False, unique=False,)

    description     = Column(String(255), nullable=True, unique=False,)

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    finder_id       = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)
    owner_id        = Column(Integer, ForeignKey('user.id'), nullable=True, unique=False)

    find_location_id    = Column(Integer, ForeignKey('location.id'), nullable=True, unique=False)
    current_location_id = Column(Integer, ForeignKey('location.id'), nullable=True, unique=False)

    image_assocs = relationship('Animal_Image_TB', backref='animal')

    related_missions = relationship('Mission_TB', backref=backref('animal', order_by=id))

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Animal_TB, self).__init__(*args, **kwargs)

class Animal_Image_TB(Base):
    __tablename__ = 'animal_image'
    __public__ = ('id', 'status', 'description',
                  'createddatetime', 'updateddatetime',
                  # foreign key
                  'animal_id', 'image_id',
                  # relationship
                  'animal', 'image'
                 )

    id              = Column(Integer, nullable=False, unique=True,
                             primary_key=True, autoincrement=True)
    animal_id = Column(Integer, ForeignKey('animal.id'), nullable=False, unique=False)
    image_id = Column(Integer, ForeignKey('image.id'), nullable=False, unique=False)

    status          = Column(String(255), nullable=False, unique=False,)
    description     = Column(String(255), nullable=True, unique=False,)

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    image = relationship('Image_TB', backref=backref('animal_assocs', order_by=id))

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Animal_Image_TB, self).__init__(*args, **kwargs)

def main():
    pass

if __name__ == '__main__':
    main()

