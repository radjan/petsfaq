from dao.person import person_dao
from service import base
class PersonService(base.GeneralService):
    def __init__(self):
        self.dao = person_dao

person_service = PersonService()
