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
import petsquarebackend.models.mission as mission_model

MISSION_RESCUE = mission_model.MISSION_RESCUE
MISSION_PICKUP = mission_model.MISSION_PICKUP
MISSION_STAY = mission_model.MISSION_STAY
MISSION_DELIVER = mission_model.MISSION_DELIVER
MISSION_ADOPT = mission_model.MISSION_ADOPT

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
    def list(self, params=None, offset=0, size=100):
        filattr = None
        if params:
            filattr = [item for item in params.items()]
        success, models = Mission_TB.list(
                                      filattr=filattr,
                                      offset=offset,
                                      size=size)

        status = self.serv_rtn(success=success, model=models)
        status['info']['count'] = len(models)
        return status

    @ServiceMethod
    def create(self, *args, **kwargs):
        real_class = TYPE_CLASS[kwargs.pop('type')]
        success, model = real_class.create(*args, **kwargs)
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

    @ServiceMethod
    def user_missions(self, user_id, params=None, offset=0, size=100):
        filattr = None
        if params:
            filattr = [item for item in params.items()]
        success, models = Mission_TB.user_missions(
                                      user_id,
                                      filattr=filattr,
                                      offset=offset,
                                      size=size)

        status = self.serv_rtn(success=success, model=models)
        status['info']['count'] = len(models)
        return status

def main():
    pass

if __name__ == '__main__':
    main()
