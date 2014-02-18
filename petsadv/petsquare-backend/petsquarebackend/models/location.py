#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
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

class Location_TB(Base):
    __tablename__ = 'location'
    __public__ = ('id','name', 'description', 'longtitude', 'latitude', 'address',
            'explorer_id',  #fk
            'explorer',     #backref
            'checks', 'missions', 'pickup_missions_from'       #relation
            'createddatetime', 'updateddatetime')


    id          = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name        = Column(String(255), nullable=True, unique=False, )
    description = Column(String(255), nullable=True, unique=False,)
    longtitude  = Column(Float(255), nullable=True, unique=False,)
    latitude    = Column(Float(255), nullable=True, unique=False,)
    address     = Column(String(255), nullable=True, unique=False,)
    #fk
    explorer_id  = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)
    #relation
    checks       = relationship('Check_TB',  backref=backref('location', order_by=id))
    found_animals = relationship('Animal_TB',
                                 backref=backref('find_location', order_by=id),
                                 foreign_keys='[Animal_TB.find_location_id]')
    animals_here = relationship('Animal_TB',
                                 backref=backref('current_location', order_by=id),
                                 foreign_keys='[Animal_TB.current_location_id]')

    missions = relationship('Mission_TB', backref=backref('dest_location', order_by=id),
                        foreign_keys='[Mission_TB.dest_location_id]')

    pickup_missions_from = relationship('MissionPickup_TB', backref=backref('from_location', order_by=id),
                        foreign_keys='[MissionPickup_TB.from_location_id]')

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Location_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, name, description, longtitude, latitude, address,
            explorer_id):
        global DBSession
        model = cls(name=name, description=description,
                longtitude=longtitude, latitude=latitude, address=address, 
                explorer_id=explorer_id)
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
    def update(cls, id, name=None, description=None, longtitude=None,
            latitude=None, address=None, explorer_id=None):
        model = cls.get_by_id(id)
        updateddatetime = datetime.datetime.now()
        log.debug('model update: %s' % model)

        #FIXME
        if name:        model.name = name
        if description: model.description = description
        if longtitude:  model.longtitude = longtitude
        if latitude:    model.latitude = latitude
        if address:     model.address = address
        if explorer_id:      model.explorer_id = explorer_id
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

