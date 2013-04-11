import webapp2

from common import share

class BoardPage(webapp2.RequestHandler):
    def get(self):
        params = {
                'hi': 'hi!!'
            }
        template = share.jinja_env.get_template('faq_board.html')
        self.response.out.write(template.render(params))
