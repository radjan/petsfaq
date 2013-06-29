import webapp2
import urllib
from google.appengine.ext import blobstore

import main
API_PREFIX = main.API_PREFIX

class upload_avatar(webapp2.RequestHandler):
    def get(self,personid):
        upload_url = blobstore.create_upload_url('%s/person/%s/avatar' % (API_PREFIX, personid))
        self.response.out.write('<html><head></head><body>')
        self.response.out.write(
            '<form action="%s" enctype="multipart/form-data" method="POST">' % upload_url)

        self.response.out.write("""
            <input type="file" name="img" /><br />
            <input type="submit" value="submit" />
            </form></body></html>
            """)

class upload_logo(webapp2.RequestHandler):
    def get(self,hospitalid):
        upload_url = blobstore.create_upload_url('%s/hospital/%s/logo' % (API_PREFIX, hospitalid))
        self.response.out.write('<html><head></head><body>')
        self.response.out.write(
            '<form action="%s" enctype="multipart/form-data" method="POST">' % upload_url)

        self.response.out.write("""
            <input type="file" name="img" /><br />
            <input type="submit" value="submit" />
            </form></body></html>
            """)
