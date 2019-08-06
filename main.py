import webapp2
import jinja2
import os
from users import OtterUser
from google.appengine.api import users
from google.appengine.ext import ndb


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        user = users.get_current_user()
        
        if user:
            email_address = user.nickname()
            logout_url = users.create_login_url('/')
            logout_html_element = '<a href = "%s">Sign out </a>' % logout_url
            self.response.write("You`re logged in as <b>" + email_address + " Don`t forget to "+ logout_html_element)
            
            otter_user = OtterUser.query().filter(OtterUser.email == email_address).get()
            
            if otter_user:
                self.response.write("Looks like you are registered. Thanks for using our site!")
            else:
                self.response.write('''
                    Welcome to our site, %s!  Please sign up! <br>
                    <form method="post" action="/">
                    <input type="text" name="otter_name">
                    <input type="submit">
                    </form><br> %s <br>
                    ''' % (email_address, logout_html_element))

                    
        else:
            login_url = users.create_login_url('/')
            login_html_element = '<a href = "%s">Sign in </a>' % login_url
            self.response.write("Please log in <b>" + login_html_element)
            
    def post(self):
        self.response.write("Welcome! " + '<a href = "/home">Home</a>' )
        
class HomeHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
    
        home_template = the_jinja_env.get_template('templates/home.html')
        # self.response.write(welcome_template.render(the_variable_dict))
        self.response.write(home_template.render())
    
    # def post(self):
    #     user = users.get_current_user()
    #     otter_user = OtterUser(
    #         otter_name=self.request.get('otter_name'),
    #         email=user.nickname())
    #     otter_user.put()
    #     self.response.write('Thanks for signing up, %s! <br><a href="/">Home</a>' %
    #         otter_user.otter_name)
            
app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/home', HomeHandler)
], debug=True)