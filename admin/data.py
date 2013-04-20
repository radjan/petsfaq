
from view import base

from service.account import account_service as acc_service
from service.person import person_service

class ListDataPage(base.BaseSessionHandler):
    @base.sa_required
    def get(self):
        accounts = acc_service.list()
        people = person_service.list()
        params = {"accounts": accounts,
                  "people": people}
        self.render_template('admin/data.html', params)
