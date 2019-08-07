import webapp2
import jinja2
import os
from users import OtterUser, OtterSetting
from google.appengine.api import users
from google.appengine.ext import ndb


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
def checkLoggedInAndRegistered(request):
    # Check if user is logged in
    
    user = users.get_current_user()
        
    if not user: 
        request.redirect("/login")
        return
    
    # Check if user is registered
       
    email_address = user.nickname()
    registered_user = OtterUser.query().filter(OtterUser.email == email_address).get()
    
    if not registered_user:
         request.redirect("/register")
         return 
    
class HomeHandler(webapp2.RequestHandler):
    def get(self):  
        checkLoggedInAndRegistered(self)
        
        the_variable_dict = {
            "logout_url":  users.create_logout_url('/')
        }
        home_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(home_template.render(the_variable_dict))

class SettingsHandler(webapp2.RequestHandler):
    def get(self):  
        checkLoggedInAndRegistered(self)
        
        settings_template = the_jinja_env.get_template('templates/settings.html')
        self.response.write(settings_template.render())

    def post(self):
        checkLoggedInAndRegistered(self)
        
        user = users.get_current_user()
        
        otter = OtterSetting(
            water_num_intake=int(self.request.get('water_num_intake')),
            food_intake=int(self.request.get('food_intake')),
            exercise=int(self.request.get('exercise')),
            bath=int(self.request.get('bath'))
        )

        otter_key = otter.put()
        self.response.write("Otter created: " + str(otter_key) + "<br>")
        self.response.write("<a href='/userotters'>All otters</a> | ")


class AllUsersHandler(webapp2.RequestHandler):
    def get(self):
        checkLoggedInAndRegistered(self)
        
        
        
        all_users = OtterSetting.query().fetch()
        
        the_variable_dict = {
            "all_users": all_users
        }
        
        all_otter_template = the_jinja_env.get_template('templates/all_users.html')
        self.response.write(all_otter_template.render(the_variable_dict))

class UserOttersHandler(webapp2.RequestHandler):
    def get(self):
        checkLoggedInAndRegistered(self)
        
        user = users.get_current_user()
        email_address = user.nickname()
        
        # user_otter = OtterSetting.query().filter(OtterSetting.owner == email_address).fetch()
        
        #the_variable_dict = {
           # "user_otter": user_otter
        #}
        
        user_otter_template = the_jinja_env.get_template('templates/user_otter.html')
        self.response.write(user_otter_template.render())
   
        

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        
        login_template = the_jinja_env.get_template('templates/login.html')
        the_variable_dict = {
            "login_url":  users.create_login_url('/')
        }
        
        self.response.write(login_template.render(the_variable_dict))
        

class RegistrationHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        registration_template = the_jinja_env.get_template('templates/registration.html')
        the_variable_dict = {
            "email_address":  user.nickname()
        }
        
        self.response.write(registration_template.render(the_variable_dict))
    
    def post(self):
        user = users.get_current_user()
        
        #Create a new CSSI User in our database
        
        otter_user = OtterUser(
            first_name=self.request.get('first_name'), 
            last_name =self.request.get('last_name'), 
            otter_name =self.request.get('otter_name'),
            email=user.nickname()
        )
        
        otter_user.put()
        
        self.response.write('Thanks for signing up, %s! <br><a href="/">Home</a>' %
        otter_user.first_name)
        
                  
    
app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/all_users', AllUsersHandler), 
    ('/user_otter', UserOttersHandler), 
    ('/login', LoginHandler),
    ('/register', RegistrationHandler),
    ('/settings', SettingsHandler)
], debug=True)