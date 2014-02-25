#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Fan 23, 2014 '
__author__= 'rad'
import logging
log = logging.getLogger(__name__)

ERROR_MODEL_OBJECT_NOT_FOUND = 'ERROR_MODEL_OBJECT_NOT_FOUND'
ERROR_RESOURCE_EXISTS = 'ERROR_RESOURCE_EXISTS'

ERROR_CODE_MAPPING = {
        ERROR_MODEL_OBJECT_NOT_FOUND: 404,
        ERROR_RESOURCE_EXISTS: 400,
    }





DEFAULT_ERROR_CODE = 500
DEFAULT_SUCCESS_CODE = 200

