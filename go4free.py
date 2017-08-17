import jinja2
import os
from google.appengine.api import users
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('home.html')
        self.response.write(template.render())

class EventsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('Events.html')
        self.response.write(template.render())

class MapHandler(webapp2.RequestHandler):
    def get (self):
        lat = self.request.get('lat')
        lng = self.request.get('lng')
        template_values = {'name':'YOUR_USER_NAME', 'lat': lat, 'lng': lng}

        template = jinja_environment.get_template('map.html')
        self.response.write(template.render(template_values))

class JobsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('Jobs.html')
        self.response.write(template.render())
class RelaxtionHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('relaxation.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Events',EventsHandler),
    ('/Career',JobsHandler),
    ('/relaxation',RelaxtionHandler),
    ('/maps',MapHandler),
], debug=True)
