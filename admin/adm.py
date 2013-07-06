from view import base

from service.account import account_service as acc_service
from service.person import person_service
from service.role import role_service

class IndexPage(base.BaseSessionHandler):
    @base.sa_required
    def get(self):
        params = {}
        self.render_template('admin/index.html', params)

class SpecialtyPage(base.BaseSessionHandler):
    @base.sa_required
    def get(self):
        params = {}
        self.render_template('admin/specialties.html', params)

