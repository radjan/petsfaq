#api
api_prefix = 'api/v'
main_version = 1
dev_version  = 2

def api_routes(config):
    #test
    config.add_route('hello','/hello')
    config.add_static_view('/apidoc', path='petsquarebackend:doc', cache_max_age=3600)

    #api
    config.add_route('locations', api_prefix + str(main_version) + '/locations')
    config.add_route('location',  api_prefix + str(main_version) + '/location/{id:\d+}')
    config.add_route('images',    api_prefix + str(main_version) + '/images')
    config.add_route('imagedata', api_prefix + str(main_version) + '/image/data/{id:\d+}')
    config.add_route('image',     api_prefix + str(main_version) + '/image/{id:\d+}')
    config.add_route('checks', api_prefix + str(main_version) + '/checks')
    config.add_route('check',  api_prefix + str(main_version) + '/check/{id:\d+}')

    

    #static pages
    #config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('/', path='petsquarebackend:web-frontend/dist', cache_max_age=3600)

