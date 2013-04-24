import webapp2

import json

from view import base
from model import *
from service.hospital import hospital_service
from common import share, util

#TODO: post and delete
class RestAPI(base.BaseSessionHandler):

    def get(self):
	#TODO: list all hospital
        result = {}
        #self.response.write(json.dump(result))

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




