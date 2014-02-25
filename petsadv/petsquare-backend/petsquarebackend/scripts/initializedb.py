#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from ..models.token import Token_TB
from ..models.mission import (
    Mission_TB,
    MissionRescue_TB,
    MissionPickup_TB,
    MissionStay_TB,
    MissionDeliver_TB,
    MissionAdopt_TB,
    MissionSupport_TB,
    Mission_User_TB
    )
from ..models import mission as mission_model


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
    #Base.metadata.create_all(engine)

    with transaction.manager as tm:

        #erase the database tables
        TABLES = (
                  Animal_Image_TB, Animal_TB,
                  Check_TB, Location_TB,
                  Mission_User_TB,
                  MissionRescue_TB, MissionPickup_TB, MissionStay_TB,
                  MissionDeliver_TB, MissionAdopt_TB, MissionSupport_TB,
                  Mission_TB,
                  Image_TB,
                  Token_TB, User_TB, Group_TB,
                 )
        for table in TABLES:
            table.__table__.drop(engine, checkfirst=True)
        Base.metadata.create_all(engine)

        #create group
        success, gmodel = Group_TB.create(
                            name='one', 
                            description='1')
        if not success:
            raise Exception(gmodel)

        #create user
        success, umodel = User_TB.create(
                            name='pub user1', 
                            description='used as public',
                            password='no password', 
                            email='fake@fake.com',
                            fb_id='1122334455667788',
                            activated=True,
                            group_id=gmodel.id)
        if not success:
            raise Exception(umodel)

        #create location
        success, lmodel1 = Location_TB.create(
                            name='one', 
                            description='1', 
                            longitude=121.5130475, 
                            latitude=25.040063, 
                            address='taipei', 
                            explorer_id=umodel.id)
        success, lmodel2 = Location_TB.create(
                            name='two', 
                            description='2', 
                            longitude=120, 
                            latitude=25.040063, 
                            address='taipei', 
                            explorer_id=umodel.id)
        success, lmodel3 = Location_TB.create(
                            name='three', 
                            description='3',
                            longitude=121.5130475, 
                            latitude=24, 
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
                            sub_type='normal',
                            status='adopted',
                            description='haha',
                            finder_id=umodel.id,
                            find_location_id=lmodel1.id)

        success, amodel2 = Animal_TB.create(name='hello kitty',
                            type='cat',
                            sub_type='kitten',
                            status='stray',
                            description='haha',
                            finder_id=umodel.id,
                            find_location_id=lmodel2.id)

        success, amodel3 = Animal_TB.create(name='jump',
                            type='dog',
                            sub_type='injected',
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

        success, m_model1 = MissionRescue_TB.create(
                             name=u'救小貓',
                             status='new',
                             completed=False,
                             place=u'新店陽光橋橋下',
                             note=u'傍晚出沒，怕人，用罐頭吸引也不會過來',
                             due_time=None,
                             reporter_id=umodel.id,
                             host_id=umodel.id,
                             animal_id=amodel2.id,
                             dest_location_id=None,
                            )

        success, m_model2 = MissionAdopt_TB.create(
                             name=u'黑白貓送養',
                             status='closed',
                             completed=True,
                             place=u'新竹',
                             note=u'卓别林賓士貓，踏雪尋梅',
                             due_time=None,
                             reporter_id=umodel.id,
                             host_id=umodel.id,
                             animal_id=amodel1.id,
                             dest_location_id=None,
                            )
        if not success:
            raise Exception(m_model2)

        success, mu_model = Mission_User_TB.create(
                             mission_id=m_model1.id,
                             user_id=umodel.id,
                             status='accepted',
                             is_owner=False,
                             description=None
                            )

        success, mu_model = Mission_User_TB.create(
                             mission_id=m_model2.id,
                             user_id=umodel.id,
                             status='assigned',
                             is_owner=True,
                             description=u'認養成功'
                            )

        if not success:
            raise Exception(mu_model)

        #create token
        success, tkmodel1 = Token_TB.create(user_id=umodel.id)
        if not success:
            raise Exception(tkmodel1)


        #create token via token service
        from ..services.token import TokenService
        service = TokenService('fake request')
        status = {}
        status = service.create(
                                user_id=umodel.id,
                                authn_by='fakebook',
                                sso_info={"key":"value", "e-mail":"abc@gm.com"},
                                )

        if not status['success']:
            raise Exception(status)
        else:
            print status

        #check via account service
        #import time; time.sleep(3)
        #from ..services.accounts import AccountService
        #service = AccountService('fake request')
        #status = service.fb_email_check(email='abc@gm.com')
        #if status['data']:
        #    status['data'] = status['data'].__json__('fake request')
        #print status

        print 'Done'
        print 'Done'
        print 'Done'
        print 'Done'
        print 'Done'
        print 'Done'
