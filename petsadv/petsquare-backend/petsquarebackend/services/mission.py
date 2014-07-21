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
from petsquarebackend.services import ServiceException
from petsquarebackend.models.mission import (
    Mission_TB,
    MissionRescue_TB,
    MissionPickup_TB,
    MissionStay_TB,
    MissionDeliver_TB,
    MissionAdopt_TB,
    MissionSupport_TB,
    )
import petsquarebackend.models.mission as mission_model

MISSION_RESCUE = mission_model.MISSION_RESCUE
MISSION_PICKUP = mission_model.MISSION_PICKUP
MISSION_STAY = mission_model.MISSION_STAY
MISSION_DELIVER = mission_model.MISSION_DELIVER
MISSION_ADOPT = mission_model.MISSION_ADOPT
MISSION_SUPPORT = mission_model.MISSION_SUPPORT

TYPE_CLASS = {
        MISSION_RESCUE: MissionRescue_TB,
        MISSION_PICKUP: MissionPickup_TB,
        MISSION_STAY: MissionStay_TB,
        MISSION_DELIVER: MissionDeliver_TB,
        MISSION_ADOPT: MissionAdopt_TB,
        MISSION_SUPPORT: MissionSupport_TB,
    }

# accpted actions
ACTION_ACCEPT = 'accept'
ACTION_ASSIGN = 'assign'
ACTION_COMPLETE = 'complete'
ACTION_QUIT = 'quit'
ACTIONS = (ACTION_ACCEPT, ACTION_ASSIGN, ACTION_COMPLETE, ACTION_QUIT)

# predefined mission status
STATUS_OPEN = 'open'
STATUS_ACCEPTED = 'accepted'
STATUS_ASSIGNED = 'assigned'
STATUS_COMPLETED = 'completed'
STATUS_CANCELED = 'canceled'

# predefined mision-user status
STATUS_MU_ACCEPTED = 'accepted'
STATUS_MU_OWNED = 'owned'
STATUS_MU_COMPLETED = 'completed'
STATUS_MU_LEAVED = 'leaved'

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
        success, model = real_class.update(id, **data)
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

    @ServiceMethod
    def link_mission_user(self, id, user_id, desc_dict):
        success, model = Mission_TB.link_mission_user(id, user_id, desc_dict)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def show_mission_user_meta(self, id, user_id):
        success, model = Mission_TB.show_mission_user_meta(id, user_id)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def update_mission_user_meta(self, id, user_id, desc_dict=None):
        if desc_dict is None:
            desc_dict = {}
        success, model = Mission_TB.update_mission_user_meta(id, user_id, desc_dict)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def unlink_mission_user(self, id, user_id):
        success, model = Mission_TB.unlink_mission_user(id, user_id)

    @ServiceMethod
    def mission_user_action(self, id, user_id, action, desc_dict=None):
        # business logic here
        # TODO object permissions: owner, host
        if desc_dict is None:
            desc_dict = {}

        sucess, mission = Mission_TB.show(id)
        if not success:
            return self.serv_rtn(success=success, model=mission)

        if action == ACTION_ACCEPT:
            if mission.status == STATUS_OPEN:
                success, model = Mission_TB.update(id, status=STATUS_ACCEPTED)
                if not success:
                    raise ServiceException(model)
            success, model = Mission_TB.link_mission_user(id,
                                                          user_id,
                                                          desc_dict)
            return self.serv_rtn(success=success, model=model)

        success, meta = Mission_TB.show_mission_user_meta(id, user_id)
        if not success:
            raise ServiceException(meta)

        m_update, mu_update = self._mission_user_action_status(mission,
                                                               meta,
                                                               action)
        desc_dict.update(mu_update)
        if m_update:
            success, model = Mission_TB.update(id, **m_update)
            if not success:
                raise ServiceException(model)

        success, model = Mission_TB.update_mission_user_meta(id,
                                                             user_id,
                                                             desc_dict)
        return self.serv_rtn(success=success, model=model)

    def _mission_user_action_status(self, mission, mission_user, action):
        '''
            missioin and mission_user status transittion by action.
        '''
        m_update = {}
        mu_update = {}
        if action == ACTION_ASSIGN:
            m_update['status'] = STATUS_ASSIGNED
            mu_update['status'] = STATUS_MU_OWNED
            mu_update['is_owner'] = True
        elif action == ACTION_COMPLETE:
            m_update['status'] = STATUS_COMPLETED
            mu_update['status'] = STATUS_MU_COMPLETED
        elif action == ACTION_QUIT:
            mu_update['status'] = STATUS_MU_LEAVED
            mu_update['is_owner'] = False
            accepters = set((mu.user_id for mu in mission.accepter_assocs))
            accepters.discard(mission_user.user_id)
            if not accepters:
                m_update['status'] = STATUS_OPEN
        else:
            raise ServiceException(util.return_dict(
                                    success=False,
                                    data='',
                                    info='Unsupported action, must be ' +
                                         '/'.join(ACTIONS),
                                    code=404)
        return m_udpate, mu_update

def main():
    pass

if __name__ == '__main__':
    main()
