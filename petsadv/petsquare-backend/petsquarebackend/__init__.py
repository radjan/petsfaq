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


#authentication
from petsquarebackend.authentication import TokenAuthenticationPolicy
from petsquarebackend.authentication import get_app_user
from pyramid.authorization import ACLAuthorizationPolicy

#add foreign key setting for sqlite, callback function
def _fk_pragma_on_connect(dbapi_con, con_record):
        dbapi_con.execute('pragma foreign_keys=ON')


def add_velruse_login_from_settings(config, settings, prefix):
    from velruse.providers.twitter import add_twitter_login
    from velruse.providers.facebook import add_facebook_login
    from velruse.settings import ProviderSettings

    #settings = config.registry.settings
    p = ProviderSettings(settings, prefix)
    p.update('consumer_key', required=True)
    p.update('consumer_secret', required=True)
    p.update('login_path')
    p.update('callback_path')
    p.update('name')

    if 'velruse.facebook.' in prefix:
        p.update('scope')
        add_facebook_login(config, **p.kwargs)
    else:
        add_twitter_login(config, **p.kwargs)
    return 


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    #authentication / authorization
    authn_policy = TokenAuthenticationPolicy()
    authz_policy = ACLAuthorizationPolicy()

    #sqlalchemy
    engine = engine_from_config(settings, 'sqlalchemy.')

    #add foreign key setting for sqlite
    event.listen(engine, 'connect', _fk_pragma_on_connect)

    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    #group-level security
    config = Configurator(settings=settings, root_factory='petsquarebackend.models.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.add_request_method(get_app_user, 'app_user', reify=True)
    config.set_authorization_policy(authz_policy)


    #add_velruse_login_from_settings(config, settings, 'velruse.twitter.web.')
    #add_velruse_login_from_settings(config, settings, 'velruse.twitter.m.')
    add_velruse_login_from_settings(config, settings, 'velruse.facebook.web.')
    add_velruse_login_from_settings(config, settings, 'velruse.facebook.m.')
    api_routes(config)

    if not config.registry.queryUtility(ISessionFactory):
        if not settings.has_key('petsquare.session_secret'):
            raise

        config.set_session_factory( \
               UnencryptedCookieSessionFactoryConfig( \
               settings.get('petsquare.session_secret')))

    config.scan()
    return config.make_wsgi_app()

