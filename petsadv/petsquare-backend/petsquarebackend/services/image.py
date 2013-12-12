#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 13, 2013 '
__author__= 'samuel'

import logging
log = logging.getLogger(__name__)

import inspect
import traceback

from petsquarebackend.services import BaseService
from petsquarebackend.services import ServiceMethod
from petsquarebackend.models.image import Image_TB

class ImageService(BaseService):
    def __init__(self, request):
        super(ImageService, self).__init__('ImageService', request)

    @ServiceMethod
    def list(self, userid=None, offset=0, size=100):
        status = self.status.copy()
        if userid:
            success, models = Image_TB.list(filattr=('userid', userid),
                                      offset=offset,
                                      size=size)
        else:
            success, models = Image_TB.list(offset=offset,
                                      size=size)

        status = self.serv_rtn(status=status, success=success, model=models)
        status['info']['count'] = len(models)
        return status

    @ServiceMethod
    def create(self, description, image, userid):
        status = self.status.copy()

        image_filename = image.filename
        image_file     = image.file

        success, model = Image_TB.create(description=description,
                                         filename=image_filename,
                                         image=image_file,
                                         userid=userid)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def show(self, id):
        status = self.status.copy()
        success, model = Image_TB.show(id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def update(self, id, data):
        status = self.status.copy()

        image_filename = data['image'].filename
        image_file     = data['image'].file

        success, model = Image_TB.update(id=id,
                           description=data['description'],
                           filename=image_filename,
                           image=image_file,
                           userid=data['userid'],)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

    @ServiceMethod
    def delete(self, id):
        status = self.status.copy()
        success, model = Image_TB.delete(id=id)
        status = self.serv_rtn(status=status, success=success, model=model)
        return status

def main():
    pass

if __name__ == '__main__':
    main()
