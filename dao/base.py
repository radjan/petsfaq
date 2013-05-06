import re
import itertools

WILDCARD = '*'

class GeneralDao:
    def get(slef, id):
        return db.get(db.Key.from_path(self.kind, int(id)))

    def create(self, m):
        m.parent = self.get_root_key()
        m.put()

    def update(self, m):
        m.put()

    def list(self):
        return self.model_cls.all()

    def search(self, kw):
        q = self.model_cls.all()
        post_filters = []
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

    def _post_query(self, q, filters):
        for f in filters:
            q = itertools.ifilter(f, q)
        return q
