import webapp2

from google.appengine.api import users

from view import base
from common import share

class BoardPage(base.BaseSessionHandler):
    def get(self):
        user = self.session.get('user')
        login = False
        name = None
        if user:
            login = True
            name = user['name']
        params = {
                'login': login,
                'name': name,
                'logout': '/logout'
            }
        template = share.jinja_env.get_template('faq_board.html')
        self.response.out.write(template.render(params))
