import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    Base,
    )

from ..models.accounts import Group_TB
from ..models.accounts import User_TB
from ..models.location import Location_TB
from ..models.image import Image_TB
from ..models.check import Check_TB

import Image as PILImage

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager as tm:
        Check_TB.__table__.drop(engine, checkfirst=True)
        Location_TB.__table__.drop(engine, checkfirst=True)
        Image_TB.__table__.drop(engine, checkfirst=True)
        User_TB.__table__.drop(engine, checkfirst=True)
        Group_TB.__table__.drop(engine, checkfirst=True)
        User_TB.__table__.drop(engine, checkfirst=True)
        Base.metadata.create_all(engine)

        #TODO: use model classmethod
        gmodel = Group_TB(name='one', description='1')
        DBSession.add(gmodel)
        DBSession.flush()

        #TODO: use model classmethod
        umodel = User_TB(name='pub user1', description='used as public',
                         password='no password', fb_api_key='fbkey',
                         fb_api_secret='apisecret', group_id=gmodel.id)
        DBSession.add(umodel)
        DBSession.flush()

        #location
        success, lmodel = Location_TB.create(name='one', description='1',
                longtitude=121.5130475, latitude=25.040063, address='taipei', explorer_id=umodel.id)
        success, lmodel = Location_TB.create(name='two', description='2',
                longtitude=121.5130475, latitude=25.040063, address='taipei', explorer_id=umodel.id)
        success, lmodel = Location_TB.create(name='three', description='3',
                longtitude=121.5130475, latitude=25.040063, address='taipei', explorer_id=umodel.id)

        #image
        f = open('petsquarebackend/scripts/python.png')
        success, imodel = Image_TB.create(description='1', 
                                          filename='python.png',
                                          image=f,
                                          uploader_id=umodel.id)

        #check
        success, cmodel = Check_TB.create(title='check1', description='1',
                location_id=lmodel.id, image_id=imodel.id, user_id=umodel.id)
        success, cmodel = Check_TB.create(title='check2', description='2',
                location_id=lmodel.id, image_id=imodel.id, user_id=umodel.id)
        success, cmodel = Check_TB.create(title='check3', description='3',
                location_id=lmodel.id, image_id=imodel.id, user_id=umodel.id)



