from view import base

from service.hospital import hospital_service

class HospitalList(base.BaseSessionHandler):
    def get(self):
        hospitals = hospital_service.list()
        self.render_template('hospitals.html', {'hospitals':hospitals})
