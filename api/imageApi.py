import webapp2
import urllib

from google.appengine.ext import blobstore, db
from google.appengine.ext.webapp import blobstore_handlers

from google.appengine.api import images
from google.appengine.api import users


from model.image import imagemodel
from model.person import Person
from model.hospital import Hospital
from model.post import Blogpost

from common import util

class Image(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, imageid):
        try:
            image = image.get_by_id(int(imageid))

            imgwidth  = self.request.get('width',  300)
            imgheight = self.request.get('height', 300)

            key = image.img_blobkey

            img = images.Image(blob_key=key)

            #resize
            img.resize(width=int(imgwidth), height=int(imgheight))
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(img.execute_transforms(output_encoding=images.PNG))

            #raw size using send_blob
            #self.send_blob(blobstore.BlobInfo.get(key))
        except:
            self.response.write({'Error':'Internal Error'})
            raise


class Avatar(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, personid):
        try:
            person = Person.get_by_id(int(personid))
            image = person.avatars.get()

            imgwidth  = self.request.get('width',  300)
            imgheight = self.request.get('height', 300)

            key = image.img_blobkey

            img = images.Image(blob_key=key)

            #resize
            img.resize(width=int(imgwidth), height=int(imgheight))
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(img.execute_transforms(output_encoding=images.PNG))

            #raw size using send_blob
            #self.send_blob(blobstore.BlobInfo.get(key))
        except:
            self.response.write({'Error':'Internal Error'})


class AvatarPost(blobstore_handlers.BlobstoreUploadHandler):
    def post(self, personid):
        try:
            imgfile = self.get_uploads('img')
            blob = imgfile[0]
            person_from_key = Person.get_by_id(int(personid))
            
            avatar = person_from_key.avatars.get()
            if avatar != None:
                avatar.img_blobkey = str(blob.key())
            else:
                avatar = imagemodel(person = person_from_key, 
                                    img_blobkey = str(blob.key()))

            putoutput = avatar.put()
            self.response.write({'personid': personid, 'imageid':putoutput.id()})
        except Exception as e:
            #self.response.write({'Error':'Internal Error'})
            self.response.write(str(e))

class Logo(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, hospitalid):
        try:
            hospital = Hospital.get_by_id(int(hospitalid))
            image = hospital.logos.get()

            imgwidth  = self.request.get('width',  300)
            imgheight = self.request.get('height', 300)

            key = image.img_blobkey

            img = images.Image(blob_key=key)

            #resize
            img.resize(width=int(imgwidth), height=int(imgheight))
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(img.execute_transforms(output_encoding=images.PNG))

            #raw size using send_blob
            #self.send_blob(blobstore.BlobInfo.get(key))
        except Exception as e:

            self.response.write({'Error':'Internal Error%s' % str(e)})
            raise

class LogoPost(blobstore_handlers.BlobstoreUploadHandler):
    def post(self, hospitalid):
        try:
            imgfile = self.get_uploads('img')
            blob = imgfile[0]
            hospital_from_key = Hospital.get_by_id(int(hospitalid))
            
            logo = hospital_from_key.logos.get()
            if logo != None:
                logo.img_blobkey = str(blob.key())
            else:
                logo = imagemodel(hospital = hospital_from_key, 
                                    img_blobkey = str(blob.key()))

            putoutput = logo.put()
            self.response.write({'hospitalid': hospitalid, 'imageid':putoutput.id()})
        except:
            self.response.write({'Error':'Internal Error'})
            raise

class Photo(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, blogpostid):
        try:
            keys = []
            blogpost = Blogpost.get_by_id(int(blogpostid))
            for image in blogpost.photos:
                keys.append(image.key().id())

            util.jsonify_response(self.response, {'imgids':keys})

        except Exception as e:
            self.response.write({'Error':'Internal Error%s' % str(e)})
            raise

class PhotoPost(blobstore_handlers.BlobstoreUploadHandler):
    def post(self, blogpostid):
        try:
            imgfiles = self.get_uploads('img')
            imgids = []

            for imgfile in imgfiles:
                blob = imgfile
                blogpost_from_key = Blogpost.get_by_id(int(blogpostid))
                
                photo = blogpost_from_key.photos.get()
                if photo != None:
                    photo.img_blobkey = str(blob.key())
                else:
                    photo = imagemodel(blogpost = blogpost_from_key, 
                                        img_blobkey = str(blob.key()))

                putoutput = photo.put()
                imgids.append(putoutput.id())
            self.response.write({'blogpostid': blogpostid, 'imageid':imgids})
        except:
            self.response.write({'Error':'Internal Error'})
            raise


