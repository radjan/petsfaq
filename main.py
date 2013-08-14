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
import view.person
from admin import data as adm_data
from admin import adm
from api import restApi
from api import specialty as specialtyApi
from api import person as personApi

from api import imageApi
from api import post as postApi
from test import testApi

from view import image
from view import post

#[BEGIN] by Zen
from view import blog
#[END]

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

global API_PREFIX
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
    ('/new_post', create.CreatePostPage),

    ('/hospitals', view.hospital.HospitalList),
    ('/createHospital', view.hospital.CreateHospital),
    webapp2.Route('/hospital/<id:\d+>', view.hospital.HospitalDetail, name='view_hospital'),
    webapp2.Route('/person/<id:\d+>', view.person.PersonDetail),
    ('/faq', faq.BoardPage),

    # edit page with privilege
    ('/hospitals/edit', view.hospital.HospitalListEdit),
    webapp2.Route('/hospital/<id:\d+>/edit',
        view.hospital.HospitalDetailEdit, name='view_hospital'),
    ('/faq', faq.BoardPage),


    ('/adm/data', adm_data.ListDataPage),
    ('/adm/index', adm.IndexPage),
    ('/adm/specialties', adm.SpecialtyPage),

    (API_PREFIX+'/hospital', restApi.HospitalAPI),
    (API_PREFIX+'/account', restApi.AccountAPI),
    (API_PREFIX+'/person', restApi.PersonAPI),
    (API_PREFIX+'/role', restApi.RoleAPI),
    (API_PREFIX+'/person/vet', personApi.VetAPI),
    (API_PREFIX+'/specialty', restApi.SpecialtyAPI),

    webapp2.Route(API_PREFIX+'/vets',                               restApi.VetAPI),
    webapp2.Route(API_PREFIX+'/admins',                             restApi.AdminAPI),

    webapp2.Route(API_PREFIX+'/hospital/<id:\d+>',                  restApi.HospitalInstanceAPI),
    webapp2.Route(API_PREFIX+'/person/<id:\d+>',                    restApi.PersonInstanceAPI),
    webapp2.Route(API_PREFIX+'/specialty/<id:\d+>',                 restApi.SpecialtyInstanceAPI),
    webapp2.Route(API_PREFIX+'/role/<id:\d+>',                      restApi.RoleInstanceAPI),

    webapp2.Route(API_PREFIX+'/specialty/<type:(species|categories)>',
                  specialtyApi.SpecialtyListAPI),

    webapp2.Route(API_PREFIX+'/hospital/<hospitalid:\d+>/specialties',
                  specialtyApi.EntitySpecialtiesAPI),
    webapp2.Route(API_PREFIX+'/vet/<vetid:\d+>/specialties',
                  specialtyApi.EntitySpecialtiesAPI),
    webapp2.Route(API_PREFIX+'/hospital/<hospitalid:\d+>/specialties/<specialtyid:\d+>',
                  specialtyApi.EntitySpecialtiesDeleteAPI),
    webapp2.Route(API_PREFIX+'/vet/<vetid:\d+>/specialties/<specialtyid:\d+>',
                  specialtyApi.EntitySpecialtiesDeleteAPI),

    #
    webapp2.Route(API_PREFIX+'/person/<personid:\d+>/avatar',       imageApi.AvatarPost, methods=['POST']),
    webapp2.Route(API_PREFIX+'/person/<personid:\d+>/avatar',       imageApi.Avatar,     methods=['GET']),
    webapp2.Route(API_PREFIX+'/person/<personid:\d+>/hospitals',    restApi.PersonHopitalList),

    webapp2.Route(API_PREFIX+'/hospital/<hospitalid:\d+>/logo',     imageApi.LogoPost,   methods=['POST']),
    webapp2.Route(API_PREFIX+'/hospital/<hospitalid:\d+>/logo',     imageApi.Logo,       methods=['GET']),
    webapp2.Route(API_PREFIX+'/blogpost/<blogpostid:\d+>/photos',   imageApi.PhotoPost,  methods=['POST']),
    webapp2.Route(API_PREFIX+'/blogpost/<blogpostid:\d+>/photos',   imageApi.Photo,      methods=['GET']),
    webapp2.Route(API_PREFIX+'/image/<imageid:\d+>',                imageApi.Image,      methods=['GET']),
    webapp2.Route(API_PREFIX+'/posts',                              postApi.BlogpostAPI),
    webapp2.Route(API_PREFIX+'/post/<blogpostid:\d+>',              postApi.PostAPI),
    webapp2.Route(API_PREFIX+'/post/<blogpostid:\d+>/attaches',     postApi.AttachedAPI),
    #webapp2.Route(API_PREFIX+'/post/<blogpostid:\d+>/attache/<attachid:\d+', postApi.AttachedItemAPI),


    webapp2.Route('/test/upload/<personid:\d+>/avatar',             image.upload_avatar, methods=['GET']),
    webapp2.Route('/test/upload/<hospitalid:\d+>/logo',             image.upload_logo,   methods=['GET']),
    webapp2.Route('/test/upload/<blogpostid:\d+>/photo',            image.upload_photo,   methods=['GET']),
    webapp2.Route('/test/upload/post',                              post.upload_post,   methods=['GET']),
    webapp2.Route('/test/upload/attaches',                          post.upload_attaches,   methods=['GET']),

    #webapp2.Route('/test/testApi/<blobid>', testApi.blob),

    #[BEGIN] by Zen,
    webapp2.Route('/blog', blog.BlogTimeline),
    #[END]

    (API_PREFIX+'/.*', NotFound),
#    (API_PREFIX+'/hospital', hospital.RestAPI),

    ('/.*', BackToMainHandler),
], config = base.myconfig, debug=DEBUG)
