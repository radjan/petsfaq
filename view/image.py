import webapp2
import urllib
from google.appengine.ext import blobstore

import main
#API_PREFIX = main.API_PREFIX

class upload_avatar(webapp2.RequestHandler):
    def get(self,personid):
        upload_url = blobstore.create_upload_url('%s/person/%s/avatar' % (main.API_PREFIX, personid))
        self.response.out.write('<html><head></head><body>')
        self.response.out.write(
            '<form action="%s" enctype="multipart/form-data" method="POST">' % upload_url)

        self.response.out.write("""
            <input type="file" name="img" /><br />
            <input type="text" value="description" name="description" /><br />
            <input type="submit" value="submit" />
            </form></body></html>
            """)

class upload_logo(webapp2.RequestHandler):
    def get(self,hospitalid):
        upload_url = blobstore.create_upload_url('%s/hospital/%s/logo' % (main.API_PREFIX, hospitalid))
        self.response.out.write('<html><head></head><body>')
        self.response.out.write(
            '<form action="%s" enctype="multipart/form-data" method="POST">' % upload_url)

        self.response.out.write("""
            <input type="file" name="img" /><br />
            <input type="text" value="description" name="description" /><br />
            <input type="submit" value="submit" />
            </form></body></html>
            """)

class upload_photo(webapp2.RequestHandler):
    def get(self,blogpostid):
        upload_url = blobstore.create_upload_url('%s/blogpost/%s/photos' % (main.API_PREFIX, blogpostid))
        self.response.out.write('<html><head></head><body>')
        self.response.out.write(
            '<form action="%s" enctype="multipart/form-data" method="POST">' % upload_url)

        self.response.out.write("""
            <input type="file" multiple="true" name="img" /><br />
            <input type="text" value="description" name="description" /><br />
            <input type="submit"  />
            </form></body></html>
            """)
