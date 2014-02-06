#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Feb 6, 2014 '
__author__= 'rad'

import logging
log = logging.getLogger(__name__)

import inspect
import traceback

from petsquarebackend.services import BaseService
from petsquarebackend.services import ServiceMethod
from petsquarebackend.models.mission import (
    Mission_TB,
    MissionRescue_TB, 
    MissionPickup_TB,
    MissionStay_TB,
    MissionDeliver_TB,
    MissionAdopt_TB,
    )

MISSION_RESCUE = 'resuce'
MISSION_PICKUP = 'pickup'
MISSION_STAY = 'stay'
MISSION_DELIVER = 'deliver'
MISSION_ADOPT = 'adopt'

TYPE_CLASS = {
        MISSION_RESCUE: MissionRescue_TB,
        MISSION_PICKUP: MissionPickup_TB,
        MISSION_STAY: MissionStay_TB,
        MISSION_DELIVER: MissionDeliver_TB,
        MISSION_ADOPT: MissionAdopt_TB, 
    }

class MissionService(BaseService):
    def __init__(self, request):
        super(MissionService, self).__init__('MissionService', request)

    @ServiceMethod
    def list(self, offset=0, size=100):
        success, models = Mission_TB.list(offset=offset,
                                      size=size)

        status = self.serv_rtn(success=success, model=models)
        status['info']['count'] = len(models)
        return status

    @ServiceMethod
    def create(cls, *args, **kwargs):
        real_class = TYPE_CLASS[kwargs.pop('type')]
        success, model = Mission_TB.create(*args, **kwargs)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def show(self, id):
        success, model = Mission_TB.show(id)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def update(self, id, data, type):
        real_class = TYPE_CLASS.get(type)
        success, model = real_class.update(**data)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def delete(self, id):
        success, model = Mission_TB.delete(id=id)
        return self.serv_rtn(success=success, model=model)

    def _get_value(self, data, key):
        return data.get(key, None)

def main():
    pass

if __name__ == '__main__':
    main()
