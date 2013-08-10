class GeneralService:
    def get(self, id):
        return self.dao.get(id);

    def create(self, h):
        return self.dao.create(h)

    def update(self, h):
        return self.dao.update(h)

    def delete(self, m):
        return self.dao.delete(m)

    def list(self):
        return self.dao.list()

    def search(self, kw, cls=None):
        return self.dao.search(kw, cls)

