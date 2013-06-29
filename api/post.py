#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import urllib

from google.appengine.ext import blobstore, db

from google.appengine.api import images
from google.appengine.api import users

from model.person import Person
from model.hospital import Hospital
from model.post import Blogpost
from view import base

class BlogpostAPI(base.BaseSessionHandler):
    def post(self):
        try:
            personid   = self.request.get('personid')
            hospitalid = self.request.get('hospitalid')
            title      = self.request.get('title')
            content    = self.request.get('content')

            person_from_key = None
            hospital_from_key = None

            if personid:
                person_from_key = Person.get_by_id(int(personid))
            if hospitalid:
                hospital_from_key = Hospital.get_by_id(int(hospitalid))

            newpost = Blogpost(title=title,
                               content=content,
                               author=person_from_key,
                               hospital=hospital_from_key)
            postoutput = newpost.put()
            self.response.write({'postid': postoutput.id()})

        except Exception as e:
            self.response.write({'Error':'Internal Error %s' % str(e)})
            raise


