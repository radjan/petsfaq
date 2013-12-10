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
        Location_TB.__table__.drop(engine, checkfirst=True)
        Base.metadata.create_all(engine)

        success, model = Location_TB.create(name='one', description='1', gps='1,5', address='taipei', userid=1)
        success, model = Location_TB.create(name='one', description='1', gps='1,5', address='taipei', userid=1)
        success, model = Location_TB.create(name='one', description='1', gps='1,5', address='taipei', userid=1)
        DBSession.add(model)

