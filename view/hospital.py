from view import base

from service.hospital import hospital_service

from common import util

class HospitalList(base.BaseSessionHandler):
    def get(self):
        hospitals = hospital_service.list()
        params = {'hospitals':hospitals,
                  'user': util.get_current_user(self.session)}
        self.render_template('hospitals.html', params)

class HospitalDetail(base.BaseSessionHandler):
    def get(self):
        h_key = self.request.get('id')
        hospital = hospital_service.get(h_key)
        params = {'hospital':hospital,
                  'user': util.get_current_user(self.session)}
        self.render_template('hospital_detail.html', params)
