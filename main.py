#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os

from google.appengine.api import users

from common import share
from view import base, faq, login

DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(DIR, 'templates')
share.jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


DEBUG = True

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        msg = ''
        if user:
            msg = 'Hi, ' + user.nickname() + ', '
        #else:
        #    self.redirect(users.create_login_url(self.request.uri))
        self.response.write(msg + 'Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', login.LoginPage),
    ('/login_google', login.GoogleLogin),
    ('/logout', login.LogoutPage),
    ('/register', login.RegisterPage),
    ('/register_idpwd', login.IdPwdRegister),
    ('/register_google', login.GoogleRegister),
    ('/faq', faq.BoardPage),
], config = base.myconfig, debug=DEBUG)
