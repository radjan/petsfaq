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

MISSION_RESCUE = 'rescue'
MISSION_PICKUP = 'pickup'
MISSION_STAY = 'stay'
MISSION_DELIVER = 'deliver'
MISSION_ADOPT = 'adopt'

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
    place           = Column(String(255), nullable=True, unique=False,)
    note            = Column(String, nullable=True, unique=False,)
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

    accepter_assocs  = relationship('Mission_User_TB',
                                    backref='mission')


    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Mission_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, *args, **kwargs):
        if cls is Mission_TB:
            raise Exception('create unknown mission type, '
                            'use child create instead')
        return cls._create(*args, **kwargs)

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
    def update(cls, *args, **kwargs):
        return cls._update(*args, **kwargs)

    @classmethod
    @ModelMethod
    def delete(cls, id):
        global DBSession
        rtn = cls.delete_by_id(id)
        return rtn

    @classmethod
    @ModelMethod
    def user_missions(cls, user_id, filattr=None, offset=None, size=None):
        global DBSession
        query = DBSession.query(cls)\
                    .join(Mission_User_TB,
                          Mission_TB.id==Mission_User_TB.mission_id)\
                    .filter(Mission_User_TB.user_id==user_id)
        return (True,
                cls.query_with_criteria(query, filattr=filattr, offset=offset,
                                        limit=size))

class MissionRescue_TB(Mission_TB):
    __tablename__ = 'mission_rescue'
    __mapper_args__ = {
        'polymorphic_identity': MISSION_RESCUE,
    }
    id = Column(Integer, ForeignKey('mission.id'), primary_key=True)

class MissionPickup_TB(Mission_TB):
    __tablename__ = 'mission_pickup'
    __public__ = tuple(list(Mission_TB.__public__) +
                       ['from_location_id',
                        'from_location'])
    __mapper_args__ = {
        'polymorphic_identity': MISSION_PICKUP,
    }
    id = Column(Integer, ForeignKey('mission.id'), primary_key=True)

    from_location_id = Column(Integer,
                              ForeignKey('location.id'),
                              nullable=True, unique=False)

class MissionStay_TB(Mission_TB):
    __tablename__ = 'mission_stay'
    __public__ = tuple(list(Mission_TB.__public__) +
                       ['period', 'skill'])
    __mapper_args__ = {
        'polymorphic_identity': MISSION_STAY,
    }
    id = Column(Integer, ForeignKey('mission.id'), primary_key=True)

    period = Column(String(255), nullable=True)
    skill = Column(String(255), nullable=True)

class MissionDeliver_TB(Mission_TB):
    __tablename__ = 'mission_deliver'
    __mapper_args__ = {
        'polymorphic_identity': MISSION_DELIVER,
    }
    id = Column(Integer, ForeignKey('mission.id'), primary_key=True)

class MissionAdopt_TB(Mission_TB):
    __tablename__ = 'mission_adopt'
    __public__ = tuple(list(Mission_TB.__public__) +
                       ['requirement'])
    __mapper_args__ = {
        'polymorphic_identity': MISSION_ADOPT,
    }
    id = Column(Integer, ForeignKey('mission.id'), primary_key=True)
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
        super(Mission_User_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, *args, **kwargs):
        return cls._create(*args, **kwargs)

    @classmethod
    @ModelMethod
    def update(cls, *args, **kwargs):
        return cls._update(*args, **kwargs)

def main():
    pass

if __name__ == '__main__':
    main()

