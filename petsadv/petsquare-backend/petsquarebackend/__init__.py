from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy import event
from petsquarebackend.routes import api_routes

from .models import (
    DBSession,
    Base,
    )

from pyramid.interfaces import (IAuthenticationPolicy,
                                IAuthorizationPolicy,
                                ISessionFactory)
from pyramid.session import UnencryptedCookieSessionFactoryConfig


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
    config.add_twitter_login_from_settings(prefix='velruse.twitter.')
    config.add_facebook_login_from_settings(prefix='velruse.facebook.')
    api_routes(config)


    if not config.registry.queryUtility(ISessionFactory):
        if not settings.has_key('petsquare.session_secret'):
            raise

        config.set_session_factory( \
               UnencryptedCookieSessionFactoryConfig( \
               settings.get('petsquare.session_secret')))

    config.scan()
    return config.make_wsgi_app()

