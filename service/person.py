
from dao.person import person_dao
class PersonService:
    def create(self, p):
        person_dao.create(p)

    def update(self, p):
        person_dao.update(p)

person_service = PersonService()
