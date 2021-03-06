#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 13, 2013 '
__author__= 'samuel'
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
import Image as PILImage
import base64

class Image_TB(Base):
    __tablename__ = 'image'
    __public__ = ('id','description','filename','image','format',
            'uploader_id',           #fk
            'uploader',              #backref
            'checks',                #relation
            'createddatetime', 'updateddatetime')

    id          = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    description = Column(String(255), nullable=True, unique=False,)
    filename    = Column(String(255), nullable=False, unique=False,)
    image       = Column(BLOB)
    format      = Column(String(20), nullable=False, unique=False,)
    #fk
    uploader_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)
    #relation
    checks      = relationship('Check_TB',  backref='image')

    createddatetime = Column(DateTime, nullable=False)
    updateddatetime = Column(DateTime, nullable=False)


    def __init__(self, *args, **kwargs):
        self.createddatetime = datetime.datetime.now()
        self.updateddatetime = datetime.datetime.now()
        super(Image_TB, self).__init__(*args, **kwargs)

    @classmethod
    @ModelMethod
    def create(cls, description, filename, image, uploader_id):
        global DBSession
        img_string = image.read()

        from io import BytesIO
        format = PILImage.open(BytesIO(img_string)).format

        model = cls(description=description,
                    filename=filename, 
                    image=base64.b64encode(img_string),
                    #image=img_string,
                    format=format,
                    uploader_id=uploader_id)
        DBSession.add(model)
        DBSession.flush()
        rtn = (True, model)
        return rtn

    @classmethod
    @ModelMethod
    def list(cls, filattr=None, offset=None, size=None):
        global DBSession
        model_list = cls.get_all(filattr=filattr, offset=offset, limit=size)
        rtn = (True, model_list)
        return rtn


    @classmethod
    @ModelMethod
    def show_img(cls, id):
        global DBSession
        model = cls.get_by_id(id)
        rtn_dict = {}
        if model != None:
            rtn_dict['format'] =  str(model.format).lower()
            rtn_dict['img'] = base64.b64decode(model.image)
        else:
            rtn_dict = None
        rtn = (True, rtn_dict)
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
    def update(cls, id, description=None, filename=filename, image=None,
            uploader_id=None):
        global DBSession
        model = cls.get_by_id(id)
        updateddatetime = datetime.datetime.now()
        log.debug('model update: %s' % model)

        #FIXME
        if description: model.description = description
        if filename:    model.filename = filename
        if image:       model.image = image
        if uploader_id:      model.uploader_id = uploader_id
        model.updateddatetime = updateddatetime
        DBSession.merge(model)
        rtn = (True, model)
        return rtn

    @classmethod
    @ModelMethod
    def delete(cls, id):
        global DBSession
        rtn = cls.delete_by_id(id)
        return rtn

    def __json__(self, request, exclude=(), extra=(), exclude_fk=True, max_depth=1):
        exclude = exclude + ('image',)
        return super(Image_TB, self).__json__(request, exclude, extra, exclude_fk, max_depth)


def main():
    pass

if __name__ == '__main__':
    main()

