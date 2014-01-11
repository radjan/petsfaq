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
    __public__ = ('id', 'name', 'type', 'status', 'description',
                  'createddatetime', 'updateddatetime', 'finder',
                  'owner', 'image_assocs')

    id              = Column(Integer, nullable=False, unique=True, 
                             primary_key=True, autoincrement=True)
    name            = Column(String(255), nullable=False, unique=False,)
    type            = Column(String(255), nullable=False, unique=False,)
    status          = Column(String(255), nullable=False, unique=False,)

    description     = Column(String(255), nullable=True, unique=False,)

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    finder_id       = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)
    owner_id        = Column(Integer, ForeignKey('user.id'), nullable=True, unique=False)

    find_location_id    = Column(Integer, ForeignKey('location.id'), nullable=True, unique=False)
    current_location_id = Column(Integer, ForeignKey('location.id'), nullable=True, unique=False)

    image_assocs = relationship('Animal_Image_TB', backref='animal')


    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Animal_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, name, type, status, description, finder_id, find_location_id=None):
        global DBSession

        model = cls(name=name,
                    type=type,
                    status=status,
                    description=description,
                    finder_id=finder_id,
                    find_location_id=find_location_id)
        DBSession.add(model)
        DBSession.flush()
        rtn = (True, model)
        return rtn

    @classmethod
    @ModelMethod
    def list(cls, filattr=None, offset=None, size=None):
        global DBSession
        model_list = cls.get_all(filattr=filattr, offset=offset, limit=size)
        rtn = (True, model_list)
        return rtn

    @classmethod
    @ModelMethod
    def show(cls, id):
        global DBSession
        model = cls.get_by_id(id)
        rtn = (True, model)
        return rtn

    @classmethod
    @ModelMethod
    def update(cls, id, name=None, type=None, status=None, description=None):
        global DBSession
        model = cls.get_by_id(id)
        updateddatetime = datetime.datetime.now()
        log.debug('model update: %s' % model)

        #FIXME
        if name:        model.name = name
        if type:        model.type = type
        if status:      model.status = status
        if description: model.description = description
        model.updateddatetime = updateddatetime
        DBSession.merge(model)
        rtn = (True, model)
        return rtn

    @classmethod
    @ModelMethod
    def delete(cls, id):
        global DBSession
        rtn = cls.delete_by_id(id)
        return rtn


class Animal_Image_TB(Base):
    __tablename__ = 'animal_image'
    __public__ = ('animal', 'image', 'status', 'description',
                  'createddatetime', 'updateddatetime')

    animal_id = Column(Integer, ForeignKey('animal.id'), primary_key=True)
    image_id = Column(Integer, ForeignKey('image.id', primary_key=True)

    status          = Column(String(255), nullable=False, unique=False,)
    description     = Column(String(255), nullable=True, unique=False,)

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    image = relationship('Image_TB', backref=backref('animal_assocs', order_by=id))

def main():
    pass

if __name__ == '__main__':
    main()

