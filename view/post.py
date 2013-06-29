import webapp2
import urllib
from view import base

import main
#API_PREFIX = main.API_PREFIX

class upload_post(base.BaseSessionHandler):
    def get(self):
        try:
            personid  = self.request.get('personid')
            hospitalid  = self.request.get('hospitalid')

            #api
            upload_url = '%s/posts' % (main.API_PREFIX,)

            self.response.out.write('<html><head></head><body>')
            self.response.out.write('Hospital ID: %s'% personid)
            self.response.out.write('Person  ID: %s'% hospitalid)
            self.response.out.write("""
                <form action="%s" enctype="multipart/form-data" method="POST">
                <label>title:</label><br />
                <input type="text" value="test_title" name="title"><br />
                <textarea rows="30" cols="30" name="content"></textarea><br />
                <input type="hidden" value="%s" name="personid">
                <input type="hidden" value="%s" name="hospitalid">
                <input type="submit" value="submit" /><br />
                </form></body></html>
                """ %(upload_url, personid, hospitalid))
        except Exception as e:
            self.response.write({'Error':'Internal Error: %s' % str(e)})

