#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.ext import blobstore

from view import base
from common import util
import main

class fileapi(base.BaseSessionHandler):
    def get(self, apiuri):
        upload_url = blobstore.create_upload_url('%s/%s' % (main.API_PREFIX, apiuri))
        util.jsonify_response(self.response,{'url': upload_url})

