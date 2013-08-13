from view import base

from common import util

class PersonDetail(base.BaseSessionHandler):
    def get(self):
        params = {'user': util.get_current_user(self.session)}
        self.render_template('person_info.html', params)
