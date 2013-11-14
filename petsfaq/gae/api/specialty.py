import json

from view import base
from service.specialty import specialty_service
from service.hospital import hospital_service
from service.role import role_service

from common import util

class SpecialtyListAPI(base.BaseSessionHandler):
    def get(self, *args, **kw):
        t = kw.get('type', '')
        if t == 'species':
            util.jsonify_response(self.response,
                                  specialty_service.list_species())
        elif t == 'categories':
            util.jsonify_response(self.response,
                                  specialty_service.list_categories())
        else:
            self.response.status = '404 Not Found'
            self.response.write('404 Not Found')

class EntitySpecialtiesAPI(base.BaseSessionHandler):
    def get(self, hospitalid=None, vetid=None):
        if hospitalid:
            m = hospital_service.get(hospitalid)
        if vetid:
            m = role_service.get(vetid)
        result = util.out_format(m.specialties)
        util.jsonify_response(self.response, result)

    def post(self, hospitalid=None, vetid=None):
        body = self.request.body
        request_json = json.loads(body)
        specialties = []
        for s in request_json:
            s = specialty_service.ensure_exist(species=s['species'],
                                               category=s['category'])
            specialties.append(s)

        h = v = None
        if hospitalid:
            h = hospital_service.get(hospitalid)
        if vetid:
            v = role_service.get(vetid)
        specialty_service.add_specialties(specialties, hospital=h, vet=v)
        self.response.status = 201
        util.jsonify_response(self.response, {"result":"ok"})

class EntitySpecialtiesDeleteAPI(base.BaseSessionHandler):
    def delete(self, hospitalid=None, vetid=None, specialtyid=None):
        s = specialty_service.get(specialtyid)
        h = v = None
        if hospitalid:
            h = hospital_service.get(hospitalid)
        if vetid:
            v = role_service.get(vetid)
        specialty_service.delete_specialty(s, hospotal=h, vet=v)

