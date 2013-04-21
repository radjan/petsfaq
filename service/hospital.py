from dao.hospital import hospital_dao as h_dao

class HospitalService:
    def create(self, h):
        return h_dao.create(h)

    def update(self, h):
        return h_dao.update(h)

    def list(self):
        return h_dao.list()

hospital_service = HospitalService()
