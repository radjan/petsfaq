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

from common import share, util
from view import base, faq, login, create
import view.hospital
from admin import data as adm_data
from api import restApi
from api import specialty as specialtyApi
from api import person as personApi

from api import imageApi
from view import image

DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(DIR, 'templates')
share.jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

DEBUG = True

class MainHandler(base.BaseSessionHandler):
    def get(self):
        self.render_template('index.html',
                             {'user': util.get_current_user(self.session)})

class BackToMainHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect('/')

class NotFound(webapp2.RequestHandler):
    def get(self):
        self.error(404)

API_PREFIX = '/api/v1'
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', login.LoginPage),
    ('/login_google', login.GoogleLogin),
    ('/logout', login.LogoutPage),
    ('/register', login.RegisterPage),
    ('/register_idpwd', login.IdPwdRegister),
    ('/register_google', login.GoogleRegister),
    (share.REG_STEP1, create.CreatePersonPage),
    (share.REG_STEP2, create.VetDetailPage),
    (share.REG_STEP3, create.WorksForPage),
    ('/new_hospital', create.CreateHospitalPage),

    ('/hospitals', view.hospital.HospitalList),
    webapp2.Route('/hospital/<id:\d+>', view.hospital.HospitalDetail, name='view_hospital'),
    ('/faq', faq.BoardPage),

    ('/adm/data', adm_data.ListDataPage),
    (API_PREFIX+'/hospital', restApi.HospitalAPI),
    (API_PREFIX+'/account', restApi.AccountAPI),
    (API_PREFIX+'/person', restApi.PersonAPI),
    (API_PREFIX+'/role', restApi.RoleAPI),
    (API_PREFIX+'/person/vet', personApi.VetAPI),
    (API_PREFIX+'/specialty', restApi.SpecialtyAPI),

    webapp2.Route(API_PREFIX+'/hospital/<id:\d+>',
                  restApi.HospitalInstanceAPI,
                  name='hospital_id'),
    webapp2.Route(API_PREFIX+'/specialty/<id:\d+>',
                  restApi.SpecialtyInstanceAPI,
                  name='specialty_id'),
    webapp2.Route(API_PREFIX+'/specialty/<type:(species|categories)>',
                  specialtyApi.SpecialtyListAPI),

    #
    webapp2.Route(API_PREFIX+'/person/<personid>/avatar',   imageApi.AvatarPost, methods=['POST']),
    webapp2.Route(API_PREFIX+'/person/<personid>/avatar',   imageApi.Avatar,     methods=['GET']),
    webapp2.Route(API_PREFIX+'/hospital/<hospitalid>/logo', imageApi.LogoPost,   methods=['POST']),
    webapp2.Route(API_PREFIX+'/hospital/<hospitalid>/logo', imageApi.Logo,       methods=['GET']),
    webapp2.Route(API_PREFIX+'/upload/<personid>/avatar',   image.upload_avatar, methods=['GET']),
    webapp2.Route(API_PREFIX+'/upload/<hospitalid>/logo',   image.upload_logo,   methods=['GET']),

    (API_PREFIX+'/.*', NotFound),
#    (API_PREFIX+'/hospital', hospital.RestAPI),

    ('/.*', BackToMainHandler),
], config = base.myconfig, debug=DEBUG)
