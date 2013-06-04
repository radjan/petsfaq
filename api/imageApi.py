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
        resource = self.request.get('blob_info_key')
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)

class ImagePost(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        imgfile = self.get_uploads('img')
        blob_info = imgfile[0]
        self.response.write('{"blob_info_key":"%s"}' % blob_info.key())

