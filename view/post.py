import webapp2
import urllib
from view import base
from common import util

import main
#API_PREFIX = main.API_PREFIX

class PostDetail(base.BaseSessionHandler):
    @base.login_required
    def get(self, *args, **kw):
        params = {'user': util.get_current_user(self.session)}
        self.render_template('post_edit.html', params)

class upload_post(base.BaseSessionHandler):
    def get(self):
        try:
            personid  = self.request.get('personid')
            hospitalid  = self.request.get('hospitalid')
            publish  = self.request.get('publish')

            #api
            upload_url = blobstore.create_upload_url('%s/posts' % (main.API_PREFIX,))

            self.response.out.write('<html><head></head><body>')
            self.response.out.write('Hospital ID: %s'% hospitalid)
            self.response.out.write('Person  ID: %s'% personid)
            self.response.out.write("""
                <form action="%s" enctype="multipart/form-data" method="POST">
                <label>title:</label><br />
                <input type="text" value="test_title" name="title"><br />
                <textarea rows="30" cols="30" name="content"></textarea><br />
                <input type="hidden" value="%s" name="personid">
                <input type="hidden" value="%s" name="hospitalid">
                <input type="hidden" value="%s" name="publish">
                <input type="submit" value="submit" /><br />
                </form></body></html>
                """ %(upload_url, personid, hospitalid, publish))
        except Exception as e:
            self.response.write({'Error':'Internal Error: %s' % str(e)})

class upload_attaches(base.BaseSessionHandler):
    def get(self):
        try:
            blogpostid = self.request.get('blogpostid')

            #api
            upload_url = blobstore.create_upload_url('%s/post/%s/attaches' % (main.API_PREFIX, blogpostid))

            self.response.out.write('<html><head></head><body>')
            self.response.out.write("""
                <form action="%s" enctype="multipart/form-data" method="POST">
                <label>title:</label><br />
                <input type="text" value="test_title" name="title"><br />
                <textarea rows="30" cols="30" name="content"></textarea><br />
                <input type="file" name="img" /><br />
                <input type="submit" value="submit" /><br />
                </form></body></html>
                """ %(upload_url ))
        except Exception as e:
            raise
            self.response.write({'Error':'Internal Error: %s' % str(e)})

