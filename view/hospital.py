from view import base

from service.hospital import hospital_service

class HospitalList(base.BaseSessionHandler):
    def get(self):
        hospitals = hospital_service.list()
        self.render_template('hospitals.html', {'hospitals':hospitals})

class HospitalDetail(base.BaseSessionHandler):
    def get(self):
        h_key = self.request.get('id')
        hospital = hospital_service.get(h_key)
        self.render_template('hospital_detail.html', {'hospital': hospital})
