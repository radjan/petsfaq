import webapp2
import urllib
from google.appengine.ext import blobstore

class upload_avatar(webapp2.RequestHandler):
    def get(self,personid):
        upload_url = blobstore.create_upload_url('/api/v1/person/%s/avatar' % personid)
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
        upload_url = blobstore.create_upload_url('/api/v1/hospital/%s/logo' % hospitalid)
        self.response.out.write('<html><head></head><body>')
        self.response.out.write(
            '<form action="%s" enctype="multipart/form-data" method="POST">' % upload_url)

        self.response.out.write("""
            <input type="file" name="img" /><br />
            <input type="submit" value="submit" />
            </form></body></html>
            """)
