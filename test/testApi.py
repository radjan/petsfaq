import logging
import webapp2
import urllib

from google.appengine.ext import blobstore, db
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import images

from common import util

class blob(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, blobid):
        try:
            print 'samuel, where I am'
            blobreader = blobstore.BlobReader(blobid,
                    buffer_size=1048576)
            value = blobreader.read()
            images.Image(value)
            print 'samuel, here I am'
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(value)
        except:
            self.response.write({'Error':'Internal Error'})
            raise
