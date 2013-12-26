from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy import event
from petsquarebackend.routes import api_routes

from .models import (
    DBSession,
    Base,
    )

#add foreign key setting for sqlite, callback function
def _fk_pragma_on_connect(dbapi_con, con_record):
        dbapi_con.execute('pragma foreign_keys=ON')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')

    #add foreign key setting for sqlite
    event.listen(engine, 'connect', _fk_pragma_on_connect)

    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    api_routes(config)
    config.scan()
    return config.make_wsgi_app()

