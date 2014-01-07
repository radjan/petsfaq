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
    with transaction.manager:
        Check_TB.__table__.drop(engine, checkfirst=True)
        Location_TB.__table__.drop(engine, checkfirst=True)
        Image_TB.__table__.drop(engine, checkfirst=True)
        Base.metadata.create_all(engine)

        #location
        success, lmodel = Location_TB.create(name='one', description='1',
                longtitude=121.5130475, latitude=25.040063, address='taipei', userid=1)
        success, lmodel = Location_TB.create(name='two', description='2',
                longtitude=121.548375, latitude=25.020945, address='taipei', userid=1)
        success, lmodel = Location_TB.create(name='three', description='3',
                longtitude=121.548732, latitude=25.102097, address='taipei', userid=1)

        #image
        f = open('petsquarebackend/scripts/python.png')
        success, imodel = Image_TB.create(description='1', 
                                          filename='python.png',
                                          image=f,
                                          userid=1)

        #check
        success, cmodel = Check_TB.create(title='check1', description='1',
                location_id=1, image_id=1, userid=1)
        success, cmodel = Check_TB.create(title='check2', description='2',
                location_id=1, image_id=1, userid=1)
        success, cmodel = Check_TB.create(title='check3', description='3',
                location_id=1, image_id=1, userid=1)


