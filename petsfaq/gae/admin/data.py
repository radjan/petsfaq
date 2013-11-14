
from view import base

from service.account import account_service as acc_service
from service.person import person_service
from service.role import role_service

class ListDataPage(base.BaseSessionHandler):
    @base.sa_required
    def get(self):
        accounts = acc_service.list()
        people = person_service.list()
        roles = role_service.list()
        params = {"accounts": accounts,
                  "people": people,
                  "roles": roles}
        self.render_template('admin/data.html', params)
