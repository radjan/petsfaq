#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import urllib
import time

from google.appengine.ext import blobstore, db
from google.appengine.ext.webapp import blobstore_handlers

from google.appengine.api import images
from google.appengine.api import users

from model.image import imagemodel
from model.person import Person
from model.hospital import Hospital
from model.post import Blogpost
from model.post import Attached
from view import base
from common import util

import json

#import main
#class file_post(base.BaseSessionHandler):
#    def get(self):
#        upload_url = blobstore.create_upload_url('%s/posts' % (main.API_PREFIX,))
#        util.jsonify_response(self.response,{'url': upload_url})
#
#
#class file_attach(base.BaseSessionHandler):
#    def get(self, postid):
#        upload_url = blobstore.create_upload_url('%s/post/%s/attaches' % (main.API_PREFIX, postid))
#        util.jsonify_response(self.response,{'url': upload_url})

class BlogpostAPI(base.BaseSessionHandler):
    """
    collection: list and create
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
            self.response.status = 201
            util.jsonify_response(self.response,{'postid': postoutput.id()})

        except Exception as e:
            self.response.write(json.dumps({'Error':'Internal Error %s' % str(e)}))
            raise

    def get(self):
        try:
            personid   = self.request.get('personid', None)
            hospitalid = self.request.get('hospitalid', None)

            postlist = Blogpost.all()
            ids = []

            if hospitalid and hospitalid.isdigit():
                #ids.append([x.key().id() for x in postlist if x.hospital.key().id() == long(hospitalid)])
                postlist = [x for x in postlist if x.hospital.key().id() == long(hospitalid)]
                ids.append(x.key().id()) 
            elif personid and personid.isdigit():
                postlist = [x for x in postlist if x.author.key().id() == long(personid)]
                ids.append(x.key().id()) 
            else:
                ids.append([x.key().id() for x in postlist])

            util.jsonify_response(self.response, {'blogpostids':ids})

        except Exception as e:
            self.response.write(json.dumps({'Error':'Internal Error %s' % str(e)}))
            raise

class PostAPI(base.BaseSessionHandler):
    """
    element: show, edit, and delete
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

            #util.jsonify_response(self.response, rtn_post)
            result = util.out_format(blogpost_from_key)
            util.jsonify_response(self.response, result)


        except Exception as e:
            self.response.write(json.dumps({'Error':'Internal Error %s' % str(e)}))
            raise

    def put(self, blogpostid):
        try:
            blogpost_from_key = Blogpost.get_by_id(int(blogpostid))

            #detail =  {'title':'unchanged',
            #           'content':'unchanged',
            #           'status_code':'unchanged'}
            detail = {}

            update = {}
            update['title']       = json.loads(self.request.body).get('title')
            update['content']     = json.loads(self.request.body).get('content')
            update['status_code'] = json.loads(self.request.body).get('publish')
            update['author']      = json.loads(self.request.body).get('personid')
            update['hospital']    = json.loads(self.request.body).get('hospitalid')
            update['post_type']   = json.loads(self.request.body).get('post_type')

            for y in [x for x in update.keys() if update[x] != None]:
                #blogpost_from_key.properties()[y].make_value_from_datastore(update[y])
                blogpost_from_key.__setattr__(y, update[y])
                detail[y] = 'Changed: %s' % update[y]

            blogpost_from_key.put()

            util.jsonify_response(self.response, detail)

        except Exception as e:
            self.response.write({'Error':'Internal Error %s' % str(e)})
            raise

    def delete(self, blogpostid):
        try:
            result = []
            blogpost_from_key = Blogpost.get_by_id(int(blogpostid))

            #delete attaches
            for x in blogpost_from_key.attaches:
                for y in x.aphotos:
                    y.delete()
                    result.append({'attach photo: %s' % y.key().id():'deleted!'})
                x.delete()
                result.append({'attach: %s' % x.key().id():'deleted!'})


            #delete photos
            for x in blogpost_from_key.photos:
                x.delete()
                result.append({'post photo: %s' % x.key().id():'deleted!'})

            #delete self
            blogpost_from_key.delete()
            result.append({'blogpost: %s' % blogpostid:'deleted!'})


            util.jsonify_response(self.response, result)

        except Exception as e:
            self.response.write(json.dumps({'Error':'Internal Error %s' % str(e)}))
            raise

class AttachesAPI(blobstore_handlers.BlobstoreUploadHandler,
                  base.BaseSessionHandler):
    """
    collection: show and edit
    """
    def get(self, blogpostid):
        try:
            blogpost_from_key = Blogpost.get_by_id(int(blogpostid))
            #ids = []
            #for x in blogpost_from_key.attaches:
            #    obj = {}
            #    obj = { x.key().id(): util.out_format(x)}
            #    ids.append(obj)
            #print 'samuel: ids %s' % ids
            #util.jsonify_response(self.response, ids)
            result = util.out_format(blogpost_from_key.attaches)
            util.jsonify_response(self.response, result)
        except Exception as e:
            raise
            self.response.write(json.dumps({'Error':'Internal Error %s' % str(e)}))

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

            #order = blogpost_from_key.attaches.count() + 1

            #post 3 args: title, content, img
            title      = self.request.get('title')
            content    = self.request.get('content')
            order      = self.request.get('order')
            imgfile    = self.get_uploads('img')

            if order.isdigit():
                order = int(order)
            else:
                order = -1

            result['order'] = order

            if len(imgfile) != 0:
                attached_type = ATYPE_PHOTO
                blob = imgfile[0]
            else:
                attached_type = ATYPE_TEXT

            #create attached
            attached = Attached(title = title, 
                                content = content,
                                attached_type = attached_type,
                                blogpost = blogpost_from_key,
                                order = order)
            attached_output = attached.put()

            result['attachedid'] = attached_output.id()

            #create photo reference to attached
            if attached_type == ATYPE_PHOTO:
                aphoto = imagemodel(description = content,
                                    attached = attached,
                                    img_blobkey = str(blob.key()))
                aphoto_output = aphoto.put()
                result['aphoto_output'] = aphoto_output.id()

            self.response.status = 201
            util.jsonify_response(self.response, result)

        except:
            raise
            self.response.write(json.dumps({'Error':'Internal Error'}))


class AttachAPI(base.BaseSessionHandler):
    """
    element: show, edit, and delete
    """
    def get(self, blogpostid, attachid):
        try:
            attach_from_key = Attached.get_by_id(int(attachid))
            if attach_from_key == None:
                result = {}
            else:
                result = util.out_format(attach_from_key)
            util.jsonify_response(self.response, result)
        except:
            self.response.write(json.dumps({'Error':'Internal Error'}))
            raise

    def put(self, blogpostid, attachid):
        try:
            attach_from_key = Attached.get_by_id(int(attachid))

            detail = {}

            update = {}
            update['title']       = json.loads(self.request.body).get('title')
            update['content']     = json.loads(self.request.body).get('content')
            update['attached_type']  = json.loads(self.request.body).get('attached_type')
            update['order']  = json.loads(self.request.body).get('order')

            for y in [x for x in update.keys() if update[x] != None]:
                attach_from_key.__setattr__(y, update[y])
                detail[y] = 'Changed: %s' % update[y]

            attach_from_key.put()
            util.jsonify_response(self.response, detail)


        except:
            self.response.write(json.dumps({'Error':'Internal Error'}))
            raise

    def delete(self, blogpostid, attachid):
        try:
            result = []
            attach_from_key = Attached.get_by_id(int(attachid))

            #delete photos
            for x in attach_from_key.aphotos:
                x.delete()
                result.append({'attach :photo: %s' % x.key().id():'deleted!'})

            #delete self
            order = attach_from_key.order
            attach_from_key.delete()
            result.append({'attach: %s' % attachid: 'deleted'})

            #re-order
            blogpost_from_key = Blogpost.get_by_id(int(blogpostid))
            for k in [x for x in blogpost_from_key.attaches if x.order > order]:
                k.order -= 1
                k.put()

            util.jsonify_response(self.response, result)

        except:
            self.response.write(json.dumps({'Error':'Internal Error'}))
            raise

