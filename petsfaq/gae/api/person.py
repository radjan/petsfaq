import webapp2

import json
from StringIO import StringIO

from view import base
from api import restApi
from service.person import person_service
from common import util


class VetAPI(base.BaseSessionHandler):
    def get(self):
        params = dict(self.request.params)
        if '_' in params:
            # add by jquery
            params.pop('_')
        people = person_service.search_vets(params)

        results = []
        for p in people:
            d = util.out_format(p, maxlevel=0)
            # XXX: vet is not a defined property
            d['vet'] = util.out_format(p.vet, maxlevel=0)
            results.append(d)

        util.jsonify_response(self.response, results)
