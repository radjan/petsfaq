#!/usr/bin/env python                                                 
# -*- coding: utf-8 -*- 

import logging
log = logging.getLogger(__name__)

class Baseview(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

