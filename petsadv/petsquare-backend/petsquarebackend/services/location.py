#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 04, 2013 '
__author__= 'samuel'

import logging
log = logging.getLogger(__name__)

import inspect
import traceback

from petsquarebackend.services import BaseService
from petsquarebackend.services import ServiceMethod
from petsquarebackend.models.location import Location_TB

class LocationService(BaseService):
    def __init__(self, request):
        super(LocationService, self).__init__('LocationService', request)

    @ServiceMethod
    def list(self, user_id=None, offset=0, size=100):
        status = self.status.copy()
        if user_id:
            success, models = Location_TB.list(filattr=('explorer_id', user_id),
                                      offset=offset,
                                      size=size)
        else:
            success, models = Location_TB.list(offset=offset,
                                      size=size)

        status = self.serv_rtn(status=status, success=success, model=models)
        status['info']['count'] = len(models)
        return status

    @ServiceMethod
    def create(self, name, description, longtitude, latitude, address, user_id):
        status = self.status.copy()
        success, model = Location_TB.create(name=name, 
                                            description=description,
                                            longtitude=longtitude,
                                            latitude=latitude,
                                            address=address, 
                                            explorer_id=user_id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def show(self, id):
        status = self.status.copy()
        success, model = Location_TB.show(id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def update(self, id, data):
        status = self.status.copy()
        success, model = Location_TB.update(id=id,
                           name=data['name'],
                           description=data['description'],
                           longtitude=data['longtitude'],
                           latitude=data['latitude'],
                           address=data['address'],
                           explorer_id=data['user_id'],)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def delete(self, id):
        status = self.status.copy()
        success, model = Location_TB.delete(id=id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

def main():
    pass

if __name__ == '__main__':
    main()
