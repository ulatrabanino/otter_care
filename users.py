from google.appengine.ext import ndb

class Otter(ndb.Model):
    otter_name = ndb.StringProperty(required=True)
    email_address = ndb.StringProperty(required=True)
    water_intake = ndb.DateTimeProperty(required=False)
    food_intake = ndb.DateTimeProperty(required=False)
    exercise = ndb.DateTimeProperty(required=False)
    bath = ndb.DateTimeProperty(required=False)

class OtterUser(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
