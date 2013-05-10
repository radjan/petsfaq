from view import base
from service.specialty import specialty_service

from common import util

class SpecialtyListAPI(base.BaseSessionHandler):
    def get(self, *args, **kw):
        t = kw.get('type', '')
        if t == 'species':
            util.jsonify_response(self.response,
                                  specialty_service.list_species())
        elif t == 'categories':
            util.jsonify_response(self.response,
                                  specialty_service.list_categories())
        else:
            self.response.status = '404 Not Found'
            self.response.write('404 Not Found')
