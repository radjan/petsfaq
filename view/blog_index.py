import webapp2
from google.appengine.api import urlfetch
import urllib
from view import base

import main
#API_PREFIX = main.API_PREFIX

class blog_index(base.BaseSessionHandler):
    def get(self):
        try:
            imgbase64  = self.request.get('imgbase64')
            content    = self.request.get('content')
            title      = self.request.get('title')

            self.response.out.write('<html><head></head><body>')
            self.response.out.write('imgbase64: %s<br />'% imgbase64)
            self.response.out.write('content: %s<br />'% content)
            self.response.out.write('title: %s<br />'% title)
            self.response.out.write('self.url: %s<br />'% self.__dict__)

            #1. post
            upload_url = '%s/posts' % (main.API_PREFIX,)
            form_fields = {
                    'content':content,
                    'title':title,
                    }
            form_data = urllib.urlencode(form_fields)
            headers = {'Content-Type':
                    'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=upload_url,
                                    payload=form_data,
                                    method=urlfetch.POST,
                                    headers=headers)
            
            self.response.out.write('result %s'%result)
            self.response.out.write('</form></body></html>')

        except Exception as e:
            self.response.write({'Error':'Internal Error: %s' % str(e)})

