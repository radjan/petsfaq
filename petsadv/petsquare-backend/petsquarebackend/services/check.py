#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 26, 2013 '
__author__= 'samuel'

import logging
log = logging.getLogger(__name__)

import inspect
import traceback

from petsquarebackend.services import BaseService
from petsquarebackend.services import ServiceMethod
from petsquarebackend.models.check import Check_TB

class CheckService(BaseService):
    def __init__(self, request):
        super(CheckService, self).__init__('CheckService', request)

    @ServiceMethod
    def list(self, user_id=None, offset=0, size=100):
        status = self.status.copy()
        if user_id:
            success, models = Check_TB.list(filattr=('user_id', user_id),
                                      offset=offset,
                                      size=size)
        else:
            success, models = Check_TB.list(offset=offset,
                                      size=size)

        status = self.serv_rtn(status=status, success=success, model=models)
        status['info']['count'] = len(models)
        return status

    @ServiceMethod
    def create(self, title, description, location_id, image_id, address, user_id):
        status = self.status.copy()
        success, model = Check_TB.create(title=title, 
                                         description=description,
                                         location_id=location_id,
                                         image_id=image_id,
                                         user_id=user_id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def show(self, id):
        status = self.status.copy()
        success, model = Check_TB.show(id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def update(self, id, data):
        status = self.status.copy()
        success, model = Check_TB.update(id=id,
                                         title=data['title'],
                                         description=data['description'],
                                         location_id=data['location_id'],
                                         image_id=data['image_id'],
                                         user_id=data['user_id'],)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def delete(self, id):
        status = self.status.copy()
        success, model = Check_TB.delete(id=id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

def main():
    pass

if __name__ == '__main__':
    main()
