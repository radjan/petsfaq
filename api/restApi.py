import webapp2

import json

from view import base
from model import *
from service.hospital import hospital_service
from service.account import account_service
from service.role import role_service
from service.person import person_service
from common import share, util

from StringIO import StringIO


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
            result[cnt] = _to_dict(i)
            cnt += 1

        io = StringIO()
        json.dump(result,io)
        self.response.write(io.getvalue())

    def post(self): # create model
        body = self.request.body
        requestJson = json.loads(body)
        kw = {}

        for i in self.model.properties() :
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


class ModelInstanceAPI(base.BaseSessionHandler):
    def get(self, *args, **kw):
        print '-'*30
        print args
        print kw
        model_id = kw.get('id', 0)
        domain_obj = self.service.get(model_id)
        domain_dict = _to_dict(domain_obj)
        io = StringIO()
        json.dump(domain_dict, io)
        self.response.write(io.getvalue())


class HospitalInstanceAPI(ModelInstanceAPI):
    def __init__(self, *args, **kw):
        self.service = hospital_service
        self.model = hospital.Hospital
        ModelInstanceAPI.__init__(self, *args, **kw)

def _to_dict(domain_obj):
    tmp = {}
    property_keys = domain_obj.properties().keys()
    for key in property_keys:
        prop = domain_obj.properties()[key]
        tmp[str(key)] = unicode(prop.get_value_for_datastore(domain_obj))
    tmp['id'] = domain_obj.key().id()
    return tmp
