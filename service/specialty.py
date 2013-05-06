from dao.specialty import specialty_dao
from service import base

SpecialtyService(base.GeneralService):
    def __init__(self, *args, **kw):
        self.dao = specialty_dao
        base.GeneralService.__init__(self, *args, **kw)

specialty_service = SpecialtyService()
