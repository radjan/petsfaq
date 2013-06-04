import webapp2
import urllib

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

from google.appengine.api import images
from google.appengine.api import users

from model.imagemodel import imagemodel

API_PREFIX = '/api/v1'

class Image(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self):
        resource  = self.request.get('blob_info_key',None)
        if resource:
            imgwidth  = self.request.get('width',  300)
            imgheight = self.request.get('height', 300)

            resource = str(urllib.unquote(resource))
            blob_info = blobstore.BlobInfo.get(resource)

            img = images.Image(blob_key=resource)

            #resize
            #------
            img.resize(width=int(imgwidth), height=int(imgheight))
            self.response.headers['Content-Type'] = 'image/jpeg'
            self.response.out.write(img.execute_transforms(output_encoding=images.JPEG))

            #raw size
            #------
            #self.send_blob(blob_info)

        else:
            self.error(404)


class ImagePost(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        imgfile = self.get_uploads('img')
        blob_info = imgfile[0]
        self.response.write('{"blob_info_key":"%s"}' % blob_info.key())
