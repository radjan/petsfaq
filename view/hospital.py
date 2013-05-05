from view import base

from service.hospital import hospital_service

from common import util

class HospitalList(base.BaseSessionHandler):
    def get(self):
        params = {'user': util.get_current_user(self.session)}
        self.render_template('hospitals.html', params)

class HospitalDetail(base.BaseSessionHandler):
    def get(self, *args, **kw):
        params = {'user': util.get_current_user(self.session)}
        self.render_template('hospital_detail.html', params)
