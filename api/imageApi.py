import webapp2
import urllib

from google.appengine.ext import blobstore, db
from google.appengine.ext.webapp import blobstore_handlers

from google.appengine.api import images
from google.appengine.api import users


from model.imagemodel import imagemodel
from model.person import Person
from model.hospital import Hospital

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
        except:
            blob.delete()
            self.response.write({'Error':'Internal Error'})

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
            blob.delete()
            self.response.write({'Error':'Internal Error'})

