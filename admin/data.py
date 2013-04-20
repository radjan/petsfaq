
from view import base

from service.account import account_service as acc_service

class ListDataPage(base.BaseSessionHandler):
    @base.sa_required
    def get(self):
        accounts = acc_service.list()
        params = {"accounts": accounts}
        self.render_template('admin/data.html', params)
