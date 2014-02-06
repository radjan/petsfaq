#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Jan 25, 2014 '
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

class Mission_TB(Base):
    __tablename__ = 'mission'
    __public__ = ('id', 'name', 'type', 'status', 'completed', 'place',
                  'note', 'due_time',
                  'createddatetime', 'updateddatetime',
                  # foreign key
                  'reporter_id', 'host_id', 'animal_id', 'dest_location_id',
                  # relationship
                  'reporter', 'host', 'animal', 'dest_location',
                  'accepter_assocs')

    id              = Column(Integer, nullable=False, unique=True, 
                             primary_key=True, autoincrement=True)
    type            = Column(String(255), nullable=False, unique=False,)
    __mapper_args__ = {
        'polymorphic_identity': 'mission',
        'polymorphic_on': type
    }
    name            = Column(String(255), nullable=False, unique=False,)
    status          = Column(String(255), nullable=False, unique=False,)
    completed       = Column(Boolean, default=False)
    places          = Column(String(255), nullable=False, unique=False,)
    note            = Column(String(255), nullable=True, unique=False,)
    due_time        = Column(DateTime, nullable=True)

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    reporter_id     = Column(Integer,
                             ForeignKey('user.id'),
                             nullable=False, unique=False)
    host_id         = Column(Integer,
                             ForeignKey('user.id'),
                             nullable=True, unique=False)

    animal_id       = Column(Integer,
                             ForeignKey('animal.id'),
                             nullable=False, unique=False)

    dest_location_id = Column(Integer,
                              ForeignKey('location.id'),
                              nullable=True, unique=False)

    accepter_assocs    = relationship('Mission_User_TB',
                                      backref='mission')


    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Mission_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, *args, **kwargs):
        if cls is Mission:
            raise Exception('create unknown mission type, '
                            'use child create instead')
        return _create(cls, *args, **kwargs)

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
    def update(cls, id, **kwargs):
        return _update(cls, id, **kwargs)

    @classmethod
    @ModelMethod
    def delete(cls, id):
        global DBSession
        rtn = cls.delete_by_id(id)
        return rtn

class MissionRescue_TB(Mission):
    __tablename__ = 'mission_rescue'
    __mapper_args__ = {
        'polymorphic_identity': 'rescue',
    }
    id = Column(Integer, ForeignKey('mission.id'), primary_key=True)

class MissionPickup_TB(Mission):
    __tablename__ = 'mission_pickup'
    __public__ = tuple(list(Mission.__public__) +
                       ['from_location_id',
                        'from_location'])
    __mapper_args__ = {
        'polymorphic_identity': 'pickup',
    }
    id = Column(Integer, ForeignKey('mission.id'), primary_key=True)

    from_location_id = Column(Integer,
                              ForeignKey('location.id'),
                              nullable=True, unique=False)

class MissionStay_TB(Mission):
    __tablename__ = 'mission_stay'
    __public__ = tuple(list(Mission.__public__) +
                       ['period', 'skill'])
    __mapper_args__ = {
        'polymorphic_identity': 'stay',
    }
    id = Column(Integer, ForeignKey('mission.id'), primary_key=True)

    period = Column(String(255), nullable=True)
    skill = Column(String(255), nullable=True)

class MissionDeliver_TB(Mission):
    __tablename__ = 'mission_deliver'
    __mapper_args__ = {
        'polymorphic_identity': 'deliver',
    }

class MissionAdopt_TB(Mission):
    __tablename__ = 'mission_adopt'
    __public__ = tuple(list(Mission.__public__) +
                       ['requirement'])
    __mapper_args__ = {
        'polymorphic_identity': 'adopt',
    }

    requirement = Column(String, nullable=True)

class Mission_User_TB(Base):
    __tablename__ = 'mission_user'
    __public__ = ('id', 'status', 'description', 'is_owner',
                  'createddatetime', 'updateddatetime',
                  # foreign key
                  'mission_id', 'user_id',
                  # relationship
                  'mission', 'user'
                 )

    id              = Column(Integer, nullable=False, unique=True,
                             primary_key=True, autoincrement=True)

    status          = Column(String(255), nullable=False, unique=False,)
    description     = Column(String(255), nullable=True, unique=False,)
    is_owner        = Column(Boolean, default=False)

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)

    mission_id      = Column(Integer,
                             ForeignKey('mission.id'),
                             nullable=False, unique=False)
    user_id         = Column(Integer,
                             ForeignKey('user.id'),
                             nullable=False, unique=False)

    user = relationship('User_TB',
                        backref=backref('mission_assocs', order_by=id))

    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Mission_Image_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, *args, **kwargs):
        return _create(cls, *args, **kwargs)

# XXX trying
def _create(cls, *args, **kwargs):
    global DBSession

    for k, v in kwargs.items():
        if isinstance(v, Base):
            kwargs.pop(k)
            # XXX assume naming convention
            kwargs[k + '_id'] = v.id
    model = cls(**kwargs)
    DBSession.add(model)
    DBSession.flush()
    rtn = (True, model)

    return rtn

# XXX trying
def _update(cls, *args, **kwargs):
    global DBSession
    model = cls.get_by_id(id)
    updateddatetime = datetime.datetime.now()
    log.debug('model update: %s' % model)

    id = args[0]
    for k, v in kwargs.items():
        if v is not None:
            model.__setattribute__(k, v)
    model.updateddatetime = updateddatetime
    DBSession.merge(model)
    rtn = (True, model)
    return rtn
    

def main():
    pass

if __name__ == '__main__':
    main()
