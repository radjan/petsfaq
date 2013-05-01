from dao.hospital import hospital_dao as h_dao
from service import base

class HospitalService(base.GeneralService):
    def __init__(self):
        self.dao = h_dao

hospital_service = HospitalService()
