import jinja2
import os
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
class JobsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('Jobs.html')
        self.response.write(template.render())
class RelaxtionHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('relaxtion.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Events',EventsHandler),
    ('/Career',JobsHandler),
    ('/relaxtion',RelaxtionHandler),
], debug=True)
