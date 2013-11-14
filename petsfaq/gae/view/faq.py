import webapp2

from google.appengine.api import users

from view import base
from common import share, util

class BoardPage(base.BaseSessionHandler):
    def get(self):
        params = { 'user': util.get_current_user(self.session) }
        template = share.jinja_env.get_template('faq_board.html')
        self.response.out.write(template.render(params))
