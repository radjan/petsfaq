import webapp2

import json
from StringIO import StringIO

from view import base
from api import restApi
from service.person import person_service


class VetAPI(base.BaseSessionHandler):
    def get(self):
        params = dict(self.request.params)
        if '_' in params:
            # add by jquery?
            params.pop('_')
        people = person_service.search_vets(params)

        results = []
        for p in people:
            d = restApi._to_dict(p)
            d['vet'] = restApi._to_dict(p.vet)
            results.append(d)

        io = StringIO()
        json.dump(results, io)
        self.response.write(io.getvalue())
