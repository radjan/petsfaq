#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import urllib
import time

from google.appengine.ext import blobstore, db
from google.appengine.ext.webapp import blobstore_handlers

from google.appengine.api import images
from google.appengine.api import users

from model.person import Person
from model.hospital import Hospital
from model.post import Blogpost
from model.post import Attached
from view import base
from common import util

import json

class BlogpostAPI(base.BaseSessionHandler):
    """
    collection: show and edit
    """
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
            self.response.write({'postid': postoutput.id()})

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
    """
    element: list and create
    """
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
            title   = json.loads(self.request.body).get('title')
            content = json.loads(self.request.body).get('content')

            result = {}
            detail = {'title':'unchanged',
                      'content':'unchanged',
                      'publish':'unchanged'}

            if title:
                blogpost_from_key.title = title
                detail['title'] = 'Changed'
            if content:
                blogpost_from_key.content = content
                detail['content'] = 'Changed'


            if publish.isdigit():
                publish = int(publish)
                blogpost_from_key.status_code = publish
                blogpost_from_key.put()
                result['result'] = {'success':detail}
                detail['publish'] = 'Changed'
            else:
                result['result'] = {'error':detail}
                detail['publish'] = 'type error'
            
            self.response.out.write(result)

        except Exception as e:
            self.response.write({'Error':'Internal Error %s' % str(e)})
            raise

class AttachedAPI(base.BaseSessionHandler, 
                  blobstore_handlers.BlobstoreUploadHandler):
    def get(self, blogpostid):
        try:
            blogpost_from_key = Blogpost.get_by_id(int(blogpostid))
            ids = []
            for x in blogpost_from_key.attaches:
                ids.append(x.key().id())
            util.jsonify_response(self.response, {'attachedids':ids})
        except Exception as e:
            raise
            self.response.write({'Error':'Internal Error %s' % str(e)})

    def post(self, blogpostid):
        try:
            result = {}

            ATYPE_TEXT = "T"
            ATYPE_PHOTO = "P"
 
            #blogpost
            hospital_from_key = None
            if blogpostid:
                blogpost_from_key = Blogpost.get_by_id(int(blogpostid))
                result['blogpostid'] = blogpostid

            #post 3 args: title, content, img
            title      = self.request.get('title')
            content    = self.request.get('content')
            imgfile    = self.get_uploads('img')

            if len(imgfile) != 0:
                attached_type = ATYPE_PHOTO
                blob = imgfile[0]
            else:
                attached_type = ATYPE_TEXT

            #create attached
            attached = Attached(title = title, 
                                content = content,
                                attached_type = attached_type,
                                blogpost = blogpost_from_key)
            attached_output = attached.put()
            result['attachedid'] = attached_output.id()

            #create photo reference to attached
            if attached_type == ATYPE_PHOTO:
                aphoto = imagemodel(description = content,
                                    attached = attached,
                                    img_blobkey = str(blob.key()))
                aphoto_output = aphoto.put()
                result['aphoto_output'] = aphoto_output.id()

            self.response.write(result)
        except:
            raise
            self.response.write({'Error':'Internal Error'})

