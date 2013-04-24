import webapp2

import json

from view import base
from model import *
from service.hospital import hospital_service
from common import share, util

from StringIO import StringIO

#TODO: post and delete
class RestAPI(base.BaseSessionHandler):

    def get(self):
	#TODO: list all hospital
        hospitals = hospital_service.list()
        result = {}
        for h in hospitals:
            result[h.name] = str(h)

        io = StringIO()
        json.dump(result,io)
        self.response.write(io.getvalue())

    def put(self):
        body = self.request.body
        requestJson = json.loads(body) 
        kw = {}    

        for i in hospital.Hospital.properties() :
            if requestJson.has_key(i):
                kw[i] = requestJson[i]

 
        aNewHospital = hospital.Hospital(**kw)
        h = hospital.Hospital(**kw)
        hospital_service.create(h)
        self.response.write('{result="ok"}')




