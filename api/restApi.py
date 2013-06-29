import webapp2

import json

from view import base
from model import *
from model import specialty
from service.hospital import hospital_service
from service.account import account_service
from service.role import role_service
from service.person import person_service
from service.specialty import specialty_service
from common import share, util


# General 
class RestAPI(base.BaseSessionHandler):

    def get(self): # get all model 
        params = dict(self.request.params)
        if '_' in params:
            # add by jquery?
            params.pop('_')
        if params:
            serviceList = self.service.search(params)
        else:
            serviceList = self.service.list()
        result = {}
        cnt = 1
        for i in serviceList: # list all model
            result[cnt] = util.output_format(i)
            cnt += 1

        util.jsonify_response(self.response, result)

    def post(self): # create model
        body = self.request.body
        requestJson = json.loads(body)
        kw = {}

        for i in self.model.properties():
            if requestJson.has_key(i):
                kw[i] = requestJson[i]

        theOne = self.model(**kw)
        self.service.create(theOne)
        self.response.write('{result="ok"}')



class HospitalAPI(RestAPI):
    service = hospital_service
    model = hospital.Hospital

class AccountAPI(RestAPI):
    service = account_service
    model = account.Account

class PersonAPI(RestAPI):
    service = person_service
    model = person.Person

class RoleAPI(RestAPI):
    service = role_service
    model = role.Role

class SpecialtyAPI(RestAPI):
    service = specialty_service
    model = specialty.Specialty

# single instance
class ModelInstanceAPI(base.BaseSessionHandler):
    def _get_obj(self, *args, **kw):
        model_id = kw.get('id', 0)
        domain_obj = self.service.get(model_id)
        domain_dict = util.out_format(domain_obj)
        return domain_obj, domain_dict

    def get(self, *args, **kw):
        _, domain_dict = self._get_obj(*args, **kw)
        util.jsonify_response(self.response, domain_object)

    def put(self, *args, **kw):
        body = self.request.body
        requestJson = json.loads(body)
        model_id = kw.get('id', 0)
        domain_obj = self.service.get(model_id)
        for i in self.model.properties():
            if requestJson.has_key(i):
                kw[i] = requestJson[i]

class HospitalInstanceAPI(ModelInstanceAPI):
    def __init__(self, *args, **kw):
        self.service = hospital_service
        self.model = hospital.Hospital
        ModelInstanceAPI.__init__(self, *args, **kw)

    def get(self, *args, **kw):
        h, h_dict = self._get_obj(*args, **kw)
        h_dict['vets'] = []
        for v in h.vets:
            # XXX Adm in vets too
            if not isinstance(v, role.Vet):
                continue
            v_dict = util.out_format(v)
            v_dict['person'] = util.out_format(v.person)
            h_dict['vets'].append(v_dict)
        util.jsonify_response(self.response, h_dict)

class SpecialtyInstanceAPI(ModelInstanceAPI):
    def __init__(self, *args, **kw):
        self.service = specialty_service
        self.model = specialty.Specialty
        ModelInstanceAPI.__init__(self, *args, **kw)

