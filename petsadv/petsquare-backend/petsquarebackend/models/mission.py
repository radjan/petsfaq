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
MISSION_SUPPORT = 'support'

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
    def user_missions(cls, user_id, filattr=None, offset=None, size=None):
        global DBSession
        query = DBSession.query(cls)\
                    .join(Mission_User_TB,
                          Mission_TB.id==Mission_User_TB.mission_id)\
                    .filter(Mission_User_TB.user_id==user_id)
        return (True,
                cls.query_with_criteria(query, filattr=filattr, offset=offset,
                                        limit=size))

    @classmethod
    @ModelMethod
    def link_mission_user(cls, id, user_id, desc_dict):
        success, assoc_obj = Mission_User_TB.get_associate_obj(id, user_id)
        if not success and assoc_obj is common.ERROR_MODEL_OBJECT_NOT_FOUND:
            desc_dict['mission_id'] = id
            desc_dict['user_id'] = user_id
            rtn = Mission_User_TB.create(**desc_dict)
        elif success:
            rtn = (False, common.ERROR_RESOURCE_EXISTS)
        else:
            rtn = (success, assoc_obj)
        return rtn

    @classmethod
    @ModelMethod
    def show_mission_user_meta(cls, id, user_id):
        return Mission_User_TB.get_associate_obj(id, user_id)

    @classmethod
    @ModelMethod
    def update_mission_user_meta(cls, id, user_id, desc_dict):
        success, assoc_obj = Mission_User_TB.get_associate_obj(id, user_id)
        if success and assoc_obj:
            desc_dict['mission_id'] = id
            desc_dict['user_id'] = user_id
            rtn = Mission_User_TB.update(assoc_obj.id, **desc_dict)
        else:
            rtn = (success, assoc_obj)
        return rtn

    @classmethod
    @ModelMethod
    def unlink_mission_user(cls, id, user_id):
        success, assoc_obj = Mission_User_TB.get_associate_obj(id, user_id)
        if success and assoc_obj:
            rtn = Mission_User_TB.delete(assoc_obj.id)
        else:
            rtn = (success, assoc_obj)
        return rtn

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

class MissionSupport_TB(Mission_TB):
    __tablename__ = 'mission_support'
    __public__ = tuple(list(Mission_TB.__public__) +
                       ['requirement', 'update'])
    __mapper_args__ = {
        'polymorphic_identity': MISSION_SUPPORT,
    }
    id = Column(Integer, ForeignKey('mission.id'), primary_key=True)
    requirement = Column(String, nullable=True)
    update = Column(String, nullable=True)

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
    def get_associate_obj(cls, mission_id, user_id):
        success, items = cls.list(filattr=[('mission_id', mission_id),
                                           ('user_id', user_id)])
        if success and items:
            if len(items) > 1:
                log.error('get_associate_obj: not unique associate'
                          ' (mission: %s, user: %s)' % (mission_id, user_id))
            return (True, items[0])
        elif success:
            return (False, common.ERROR_MODEL_OBJECT_NOT_FOUND)
        else:
            return (success, items)

def main():
    pass

if __name__ == '__main__':
    main()

