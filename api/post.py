#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import urllib
import time

from google.appengine.ext import blobstore, db

from google.appengine.api import images
from google.appengine.api import users

from model.person import Person
from model.hospital import Hospital
from model.post import Blogpost
from view import base
from common import util

import json

class BlogpostAPI(base.BaseSessionHandler):
    def post(self):
        try:
            personid   = self.request.get('personid')
            hospitalid = self.request.get('hospitalid')
            title      = self.request.get('title')
            content    = self.request.get('content')
            publish    = self.request.get('publish')

            person_from_key = None
            hospital_from_key = None

            if personid:
                person_from_key = Person.get_by_id(int(personid))
            if hospitalid:
                hospital_from_key = Hospital.get_by_id(int(hospitalid))

            if publish.isdigit():
                publish = int(publish)
            else:
                publish = None

            newpost = Blogpost(title=title,
                               content=content,
                               author=person_from_key,
                               hospital=hospital_from_key,
                               status_code=publish)

            postoutput = newpost.put()
            self.response.status = 201
            util.jsonify_response(self.response, {'postid': postoutput.id(), "result":"ok"})
            #self.response.write({'postid': postoutput.id()})

        except Exception as e:
            self.response.write({'Error':'Internal Error %s' % str(e)})
            raise

    def get(self):
        try:
            ids = []
            for x in Blogpost.all():
                ids.append(x.key().id())
            util.jsonify_response(self.response, {'blogpostids':ids})
        except Exception as e:
            self.response.write({'Error':'Internal Error %s' % str(e)})
            raise

class PostAPI(base.BaseSessionHandler):
    def get(self, blogpostid):
        try:
            blogpost_from_key = Blogpost.get_by_id(int(blogpostid))

            authorid = None
            hospitalid = None

            if blogpost_from_key.author:
                authorid = blogpost_from_key.author.key().id()
            if blogpost_from_key.hospital:
                hospitalid = blogpost_from_key.hospital.key().id()

            created = blogpost_from_key.created
            created = str(long(time.mktime(created.timetuple())))
            last_modified = blogpost_from_key.last_modified
            last_modified = str(long(time.mktime(last_modified.timetuple())))

            status_code = blogpost_from_key.status_code

            rtn_post = {}
            rtn_post.update({'title':blogpost_from_key.title})
            rtn_post.update({'authorid':authorid})
            rtn_post.update({'hospitalid':hospitalid})
            rtn_post.update({'content':blogpost_from_key.content})
            rtn_post.update({'created':created})
            rtn_post.update({'last_modified':last_modified})
            rtn_post.update({'status_code':status_code})

            photos = []
            for x in blogpost_from_key.photos:
                photos.append(x.key().id())
            rtn_post.update({'photoids':photos})

            util.jsonify_response(self.response, rtn_post)

        except Exception as e:
            self.response.write({'Error':'Internal Error %s' % str(e)})
            raise

    def put(self, blogpostid):
        try:
            blogpost_from_key = Blogpost.get_by_id(int(blogpostid))
            publish = json.loads(self.request.body).get('publish')

            if publish.isdigit():
                publish = int(publish)
                blogpost_from_key.status_code=publish
                blogpost_from_key.put()
                self.response.out.write('status_code changed to %s OK!'% publish)
            else:
                self.response.out.write('no changed')

        except Exception as e:
            self.response.write({'Error':'Internal Error %s' % str(e)})
            raise


