import webapp2

import json

from view import base
from model import specialty, person, hospital, account, role
from service.hospital import hospital_service
from service.account import account_service
from service.role import role_service
from service.person import person_service
from service.specialty import specialty_service
from common import share, util
from sets import Set


# General 
class RestAPI(base.BaseSessionHandler):

    def get(self): # get all model 
        params = dict(self.request.params)
        if '_' in params:
            # add by jquery
            params.pop('_')
        if params:
            serviceList = self.service.search(params)
        else:
            serviceList = self.service.list()

        result = util.out_format(serviceList)
        util.jsonify_response(self.response, result)

    def post(self): # create model
        body = self.request.body
        requestJson = json.loads(body)

        new_id = self._create(requestJson)
        self.response.status = 201
        util.jsonify_response(self.response, {'id': new_id, "result":"ok"})

    def _create(self, requestJson):
        #overwrite this if the creation needs to be customized
        kw = util.get_model_properties(self.model, requestJson)
        theOne = self.model(**kw)
        return self.service.create(theOne)

class HospitalAPI(RestAPI):
    service = hospital_service
    model = hospital.Hospital

    def _create(self, requestJson):
        specialties = []
        if 'specialties' in requestJson:
            specialties = requestJson.pop('specialties')

        kw = util.get_model_properties(self.model, requestJson)
        theOne = self.model(**kw)
        new_id = self.service.create(theOne)

        for s in specialties:
            s = specialty_service.ensure_exist(s['species'], s['category'])
            specialty_service.add_specialty(s, hospital=theOne)
        return new_id

class AccountAPI(RestAPI):
    service = account_service
    model = account.Account

class PersonAPI(RestAPI):
    service = person_service
    model = person.Person

class RoleAPI(RestAPI):
    service = role_service
    model = role.Role

    def _create(self, requestJson):
        specialties = []
        if 'specialties' in requestJson:
            specialties = requestJson.pop('specialties')

        kw = util.get_model_properties(self.model, requestJson)
        theOne = self.model(**kw)
        new_id = self.service.create(theOne)

        for s in specialties:
            s = specialty_service.ensure_exist(s['species'], s['category'])
            specialty_service.add_specialty(s, vet=theOne)
        return new_id

class SpecialtyAPI(RestAPI):
    service = specialty_service
    model = specialty.Specialty

class VetAPI(RestAPI):
    service = role_service
    model = role.Vet

    def _create(self, requestJson):
        specialties = []
        if 'specialties' in requestJson:
            specialties = requestJson.pop('specialties')

        p_dict = requestJson['person']
        if isinstance(p_dict, dict) and 'id' not in p_dict:
            pkw = util.get_model_properties(person.Person, p_dict)
            p = person.Person(**pkw)
            person_service.create(p)
            requestJson['person'] = p
        kw = util.get_model_properties(self.model, requestJson)
        theOne = self.model(**kw)
        new_id = self.service.create(theOne)

        for s in specialties:
            s = specialty_service.ensure_exist(s['species'], s['category'])
            specialty_service.add_specialty(s, vet=theOne)
        return new_id

class AdminAPI(RestAPI):
    service = role_service
    model = role.Admin

    def _create(self, requestJson):
        p_dict = requestJson['person']
        if isinstance(p_dict, dict) and 'id' not in p_dict:
            pkw = util.get_model_properties(person.Person, p_dict)
            p = person.Person(**pkw)
            person_service.create(p)
            requestJson['person'] = p
        kw = util.get_model_properties(self.model, requestJson)
        theOne = self.model(**kw)
        return self.service.create(theOne)

# single instance
class ModelInstanceAPI(base.BaseSessionHandler):
    def _get_obj(self, *args, **kw):
        model_id = kw.get('id', 0)
        domain_obj = self.service.get(model_id)
        domain_dict = util.out_format(domain_obj)
        return domain_obj, domain_dict

    def get(self, *args, **kw):
        _, domain_dict = self._get_obj(*args, **kw)
        util.jsonify_response(self.response, domain_dict)

    def put(self, *args, **kw):
        body = self.request.body
        requestJson = json.loads(body)
        model_id = kw.get('id', 0)
        domain_obj = self.service.get(model_id)
        if not domain_obj:
            self.error(404)
            return

        domain_obj = self._custom_update(domain_obj, requestJson)
        # partial update
        domain_obj = util.update_model_properties(domain_obj, requestJson)
        self.service.update(domain_obj)
        util.jsonify_response(self.response, {"result":"ok"})

    def delete(self, *args, **kw):
        model_id = int(kw.get('id', 0))
        if model_id:
            self.service.delete(model_id)
        util.jsonify_response(self.response, {"result":"ok"})

    def _custom_update(self, domain_obj, _requestJson):
        return domain_obj

class HospitalInstanceAPI(ModelInstanceAPI):
    def __init__(self, *args, **kw):
        self.service = hospital_service
        self.model = hospital.Hospital
        ModelInstanceAPI.__init__(self, *args, **kw)

    def _custom_update(self, hospital, requestJson):
        if 'specialties' in requestJson:
            specialties = requestJson.pop('specialties')
            specialty_service.overwrite_specialties(specialties, hospital=hospital)
        return hospital

class PersonInstanceAPI(ModelInstanceAPI):
    def __init__(self, *args, **kw):
        self.service = person_service
        self.model = person.Person
        ModelInstanceAPI.__init__(self, *args, **kw)

class SpecialtyInstanceAPI(ModelInstanceAPI):
    def __init__(self, *args, **kw):
        self.service = specialty_service
        self.model = specialty.Specialty
        ModelInstanceAPI.__init__(self, *args, **kw)

class RoleInstanceAPI(ModelInstanceAPI):
    def __init__(self, *args, **kw):
        self.service = role_service
        self.model = role.Role
        ModelInstanceAPI.__init__(self, *args, **kw)

    def _custom_update(self, role, requestJson):
        if 'specialties' in requestJson:
            specialties = requestJson.pop('specialties')
            specialty_service.overwrite_specialties(specialties, vet=role)
        return hospital

class PersonHopitalList(RestAPI):
    service = person_service
    model = person.Person
    def get(self, personid):
        try:
            person_from_key = self.model.get_by_id(int(personid))

            if person_from_key:
                 roles = person_from_key.roles

            hospitals = {}
            hospitalids = Set()
            rtn_list = []
            for r in roles:
                if r:
                    hospitals.update({r.hospital.get_id():r.hospital})
                    hospitalids.add(r.hospital.get_id())

            for hid in list(hospitalids):
                rtn_list.append(hospitals[hid])

            util.jsonify_response(self.response,util.out_format(rtn_list))

        except:
            self.response.write({'Error':'Internal Error'})
            raise



