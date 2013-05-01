from dao.hospital import hospital_dao as h_dao

class HospitalService:

    def get(self, id):
        return h_dao.get(id);

    def create(self, h):
        return h_dao.create(h)

    def update(self, h):
        return h_dao.update(h)

    def list(self):
        return h_dao.list()

    def search(self, kw):
        return h_dao.search(kw)

hospital_service = HospitalService()
