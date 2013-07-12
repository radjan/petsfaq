from google.appengine.ext import db

from model import hospital as h_model
from dao import base
from common import share

get_root_key = share.org_root_key
KIND = 'Hospital'

class HospitalDao(base.GeneralDao):
    def __init__(self):
        self.model_cls = h_model.Hospital

hospital_dao = HospitalDao()
