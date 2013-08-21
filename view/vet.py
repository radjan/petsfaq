from view import base

# from service.hospital import hospital_service

from common import util

class CreateVet(base.BaseSessionHandler):
    def get(self):
        params = {'user': util.get_current_user(self.session)}
        self.render_template('create_vet.html', params)