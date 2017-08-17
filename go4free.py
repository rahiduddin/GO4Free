import jinja2
import os
from google.appengine.api import users
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            #greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' % (user.nickname(), users.create_logout_url('/')))
            template = jinja_environment.get_template('home.html')
            self.response.write(template.render({'user': user, 'users': users}))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.write('<html><body>%s</body></html>' % greeting)


        #template = jinja_environment.get_template('home.html')
        #self.response.write(template.render())

class EventsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('Events.html')
        self.response.write(template.render())

class JobsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('Jobs.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Events',EventsHandler),
    ('/Career',JobsHandler),
], debug=True)
