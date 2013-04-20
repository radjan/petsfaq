
from dao.person import person_dao
class PersonService:
    def create(self, p):
        return person_dao.create(p)

    def update(self, p):
        return person_dao.update(p)

    def list(self):
        return person_dao.list()

person_service = PersonService()
