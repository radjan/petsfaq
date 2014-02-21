#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Jan 23, 2014 '
__author__= 'rad'

import logging
log = logging.getLogger(__name__)

import inspect
import traceback

from petsquarebackend.services import BaseService
from petsquarebackend.services import ServiceMethod
from petsquarebackend.models.animal import Animal_TB

class AnimalService(BaseService):
    def __init__(self, request):
        super(AnimalService, self).__init__('AnimalService', request)

    @ServiceMethod
    def list(self, finder_id, offset=0, size=100):
        if finder_id:
            success, models = Animal_TB.list(filattr=('finder_id', finder_id),
                                      offset=offset,
                                      size=size)
        else:
            success, models = Animal_TB.list(offset=offset,
                                      size=size)

        status = self.serv_rtn(success=success, model=models)
        status['info']['count'] = len(models)
        return status

    @ServiceMethod
    def create(self, animal_dict):
        # XXX not consistent with other, try to simplify the signature
        success, model = Animal_TB.create(**animal_dict)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def show(self, id):
        success, model = Animal_TB.show(id)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def update(self, id, data):
        success, model = Animal_TB.update(id=id,
                           name=data.get('name', None),
                           type=data.get('type', None),
                           sub_type=data.get('sub_type', None),
                           description=data.get('description', None),
                           finder_id=data.get('finder_id', None),
                           find_location_id=data.get('find_location_id', None),)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def delete(self, id):
        success, model = Animal_TB.delete(id=id)
        return self.serv_rtn(success=success, model=model)

def main():
    pass

if __name__ == '__main__':
    main()
