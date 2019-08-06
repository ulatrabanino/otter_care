import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
<<<<<<< HEAD
class MainPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(welcome_template.render())
        

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
=======
>>>>>>> dad331143626ea61fcd8471fe704b4f08c6d85fa
