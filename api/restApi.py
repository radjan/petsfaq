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
	#TODO: list all hospital
        serviceList = self.service.list()
        result = {}
        cnt = 1
        for i in serviceList: # list all model
            tmp = {} 
            property_keys = i.properties().keys()
            for key in property_keys: 
                tmp[str(key)] = unicode(i.properties()[key].get_value_for_datastore(i))
            result[cnt] = tmp
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


