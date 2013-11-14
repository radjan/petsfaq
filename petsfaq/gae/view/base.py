import webapp2
from webapp2_extras import sessions

from common import share

#This is needed to configure the session secret key
#Runs first in the whole application
myconfig = {}
myconfig['webapp2_extras.sessions'] = {
    'secret_key': share.WEBAPP2_SESSION_KEY,
}

# TODO csrf protect
class BaseSessionHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    def render_template(self, template_path, params=None):
        if params is None:
            params = {}
        template = share.jinja_env.get_template(template_path)
        self.response.out.write(template.render(params))

def login_required(handler):
    """
         Decorator for checking if there's a user associated with the current session.
         Will also fail if there's no session present.
     """

    def check_login(self, *args, **kwargs):
        if 'user' not in self.session:
            # If handler has no login_url specified invoke a 403 error
            try:
                self.redirect('/login', abort=True)
            except (AttributeError, KeyError), e:
                self.abort(403)
        else:
            return handler(self, *args, **kwargs)

    return check_login

def sa_required(handler):
    """
         Decorator for checking if there's a user associated with the current session.
         Will also fail if there's no session present.
     """

    def check_sa(self, *args, **kwargs):
        # TODO: check system admin
        if 'user' not in self.session:
            # If handler has no login_url specified invoke a 403 error
            try:
                self.redirect('/login', abort=True)
            except (AttributeError, KeyError), e:
                self.abort(403)
        else:
            return handler(self, *args, **kwargs)
    return check_sa
