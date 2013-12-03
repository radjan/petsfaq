#api
api_prefix = 'api/v'
main_version = 1
dev_version  = 2

def api_routes(config):
    #test
    config.add_route('hello','/hello')


    #api
    config.add_route('locations',  api_prefix + str(main_version) + '/locations')
    config.add_route('locationid', api_prefix + str(main_version) + '/location/{id:\d+}')

    

    #static pages
    #config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('/', path='petsquarebackend:web-frontend/dist', cache_max_age=3600)

