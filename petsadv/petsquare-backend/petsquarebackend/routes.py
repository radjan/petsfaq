#api
api_prefix = 'api/v'
app_prefix = 'app/v'
main_version = 1
dev_version  = 2

def api_routes(config):
    #test
    config.add_route('hello','/hello')
    config.add_static_view('/apidoc', path='petsquarebackend:doc', cache_max_age=3600)

    #api
    config.add_route('locations',     api_prefix + str(main_version) + '/locations')
    config.add_route('location',      api_prefix + str(main_version) + '/location/{id:\d+}')
    config.add_route('images',        api_prefix + str(main_version) + '/images')
    config.add_route('imagedata',     api_prefix + str(main_version) + '/image/data/{id:\d+}')
    config.add_route('image',         api_prefix + str(main_version) + '/image/{id:\d+}')
    config.add_route('checks',        api_prefix + str(main_version) + '/checks')
    config.add_route('check',         api_prefix + str(main_version) + '/check/{id:\d+}')
    config.add_route('animals',       api_prefix + str(main_version) + '/animals')
    config.add_route('animal',        api_prefix + str(main_version) + '/animal/{id:\d+}')
    config.add_route('missions',      api_prefix + str(main_version) + '/missions')
    config.add_route('mission',       api_prefix + str(main_version) + '/mission/{id:\d+}')

    #app

    config.add_route('app-showme',    app_prefix + str(main_version) + '/user/me')
    config.add_route('app-locations', app_prefix + str(main_version) + '/locations')
    config.add_route('app-location',  app_prefix + str(main_version) + '/location/{id:\d+}')
    config.add_route('app-animals',   app_prefix + str(main_version) + '/animals')
    config.add_route('app-animal',    app_prefix + str(main_version) + '/animal/{id:\d+}')
    config.add_route('app-checks',    app_prefix + str(main_version) + '/checks')
    config.add_route('app-check',     app_prefix + str(main_version) + '/check/{id:\d+}')
    config.add_route('app-images',    app_prefix + str(main_version) + '/images')
    config.add_route('app-imagedata', app_prefix + str(main_version) + '/image/data/{id:\d+}')
    config.add_route('app-image',     app_prefix + str(main_version) + '/image/{id:\d+}')
    config.add_route('app-missions',  app_prefix + str(main_version) + '/missions')
    config.add_route('app-mission',   app_prefix + str(main_version) + '/mission/{id:\d+}')





    #non-version
    config.add_route('app-ssologout-facebook', 'm/ssologout/facebook')

    config.add_route('app-login-facebook',     'm/login/facebook')
    config.add_route('app-logout-facebook',    'm/logout/facebook')

    #static pages
    #config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('/', path='petsquarebackend:web-frontend/dist', cache_max_age=3600)

