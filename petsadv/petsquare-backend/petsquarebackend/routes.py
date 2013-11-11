
def api_routes(config):
    config.add_route('hello','/hello')

    #static pages
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

