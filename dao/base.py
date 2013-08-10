import re
import itertools

from google.appengine.ext import db

WILDCARD = '*'

class GeneralDao:
    def get(self, id):
        return self.model_cls.get_by_id(int(id))

    def create(self, m):
        m.parent = self.get_root_key()
        m.put()
        return m.get_id()

    def update(self, m):
        m.put()

    def delete(self, m):
        if type(m) == int:
            m = self.get(m)
        m.key.delete()

    def list(self):
        return self.model_cls.all()

    def search(self, kw, cls=None):
        q = self.model_cls.all()

        post_filters = []
        if cls:
            post_filters.append(self._class_filter(cls))

        for name, query in kw.items():
            if WILDCARD in query:
                post_filters.append(self._post_like_filter(name, query))
            else:
                q.filter('%s =' % name, query)
        q = self._post_query(q, post_filters)
        return q

    def _post_like_filter(self, property_name, qs):
        sre = re.compile(qs.replace(WILDCARD, '.*'))
        def f(model):
            if sre.match(model.__getattribute__(property_name)):
                return True
            return False
        return f

    def _class_filter(self, cls):
        return lambda model: isinstance(model, cls)

    def _post_query(self, q, filters):
        for f in filters:
            q = itertools.ifilter(f, q)
        return q
