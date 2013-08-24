from view import base

from common import util

class BlogTimeline(base.BaseSessionHandler):
    def get(self):
        params = {'user': util.get_current_user(self.session)}
        self.render_template('blog/timeline.html')

class PostView(base.BaseSessionHandler):
    def get(self):
        params = {'user': util.get_current_user(self.session)}
        self.render_template('post_edit.html')
        
class Test():
     def get(self):
        params = {'user': util.get_current_user(self.session)}
        name = self.request.get('name')
        self.response.out.write(name)