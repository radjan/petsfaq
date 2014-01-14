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
from ..models.animal import Animal_TB, Animal_Image_TB

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

        #erase the database tables
        Animal_Image_TB.__table__.drop(engine, checkfirst=True)
        Check_TB.__table__.drop(engine,    checkfirst=True) #  ^
        Location_TB.__table__.drop(engine, checkfirst=True) #  |
        Image_TB.__table__.drop(engine,    checkfirst=True) #  |
        User_TB.__table__.drop(engine,     checkfirst=True) #  |
        Group_TB.__table__.drop(engine,    checkfirst=True) #  |
        User_TB.__table__.drop(engine,     checkfirst=True) #  |
        Animal_TB.__table__.drop(engine,   checkfirst=True) #  |
        Base.metadata.create_all(engine)

        success = True
        #create group
        success, gmodel = Group_TB.create(
                            name='one', 
                            description='1')
        if not success: return
            raise Exception(gmodel)

        #create user
        success, umodel = User_TB.create(
                            name='pub user1', 
                            description='used as public',
                            password='no password', 
                            fb_api_key='fbkey',
                            fb_api_secret='apisecret', 
                            group_id=gmodel.id)
        if not success:
            raise Exception(umodel)

        #create location
        success, lmodel1 = Location_TB.create(
                            name='one', 
                            description='1', 
                            longtitude=121.5130475, 
                            latitude=25.040063, 
                            address='taipei', 
                            explorer_id=umodel.id)
        success, lmodel2 = Location_TB.create(
                            name='two', 
                            description='2', 
                            longtitude=121.5130475, 
                            latitude=25.040063, 
                            address='taipei', 
                            explorer_id=umodel.id)
        success, lmodel3 = Location_TB.create(
                            name='three', 
                            description='3',
                            longtitude=121.5130475, 
                            latitude=25.040063, 
                            address='taipei', 
                            explorer_id=umodel.id)
        if not success:
            raise Exception(lmodel3)
            
        #create image
        f = open('petsquarebackend/scripts/python.png')
        success, imodel1 = Image_TB.create(
                            description='Fly Python', 
                            filename='python.png',
                            image=f,
                            uploader_id=umodel.id)
        f.close()
        f = open('petsquarebackend/scripts/xkcd-style-plots.png')
        success, imodel2 = Image_TB.create(
                            description='xkcd style plots', 
                            filename='plot.png',
                            image=f,
                            uploader_id=umodel.id)
        if not success:
            raise Exception(imodel2)
        #create check
        success, cmodel = Check_TB.create(
                            title='check1', 
                            description='1', 
                            location_id=lmodel1.id, 
                            image_id=imodel1.id, 
                            user_id=umodel.id)
        success, cmodel = Check_TB.create(
                            title='check2', 
                            description='2', 
                            location_id=lmodel2.id, 
                            image_id=imodel1.id, 
                            user_id=umodel.id)
        success, cmodel = Check_TB.create(
                            title='check3', 
                            description='3', 
                            location_id=lmodel3.id, 
                            image_id=imodel2.id, 
                            user_id=umodel.id)
        if not success:
            raise Exception(cmodel)

        success, amodel1 = Animal_TB.create(name='pochi',
                            type='cat',
                            status='adopted',
                            description='haha',
                            finder_id=umodel.id,
                            find_location_id=lmodel.id)

        success, amodel2 = Animal_TB.create(name='hello kitty',
                            type='cat',
                            status='halfway',
                            description='haha',
                            finder_id=umodel.id,
                            find_location_id=lmodel2.id)

        success, amodel3 = Animal_TB.create(name='jump',
                            type='dog',
                            status='halfway',
                            description='haha',
                            finder_id=umodel.id,
                            find_location_id=lmodel3.id)

        if not success:
            raise Exception(amodel3)

        success, aimodel = Animal_Image_TB.create(
                            status='halfway',
                            description='XD',
                            animal=amodel1,
                            image=imodel1)

        success, aimodel = Animal_Image_TB.create(
                            status='adopted',
                            description='XD',
                            animal=amodel1,
                            image=imodel2)

        success, aimodel = Animal_Image_TB.create(
                            status='halfway',
                            description='XD',
                            animal=amodel2,
                            image=imodel1)
        if not success:
            raise Exception(aimodel)
