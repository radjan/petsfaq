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
    def list(self, params=None, offset=0, size=100):
        filattr = None
        if params:
            filattr = [item for item in params.items()]
        success, models = Animal_TB.list(filattr=filattr,
                                         offset=offset,
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
        success, model = Animal_TB.update(id, **data)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def delete(self, id):
        success, model = Animal_TB.delete(id=id)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def link_image(self, id, image_id, desc_dict=None):
        if desc_dict is None:
            desc_dict = {}
        success, model = Animal_TB.link_image(id, image_id, desc_dict)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def show_image_meta(self, id, image_id):
        success, model = Animal_TB.show_image_meta(id, image_id)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def update_image_meta(self, id, image_id, desc_dict=None):
        if desc_dict is None:
            desc_dict = {}
        success, model = Animal_TB.update_image_meta(id, image_id, desc_dict)
        return self.serv_rtn(success=success, model=model)

    @ServiceMethod
    def unlink_image(self, id, image_id, desc_dict=None):
        if desc_dict is None:
            desc_dict = {}
        success, model = Animal_TB.unlink_image(id, image_id, desc_dict)
        return self.serv_rtn(success=success, model=model)

def main():
    pass

if __name__ == '__main__':
    main()
