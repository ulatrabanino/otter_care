from google.appengine.ext import ndb

class Otter(ndb.Model):
    otter_name = ndb.StringProperty(required=True)
    email_address = ndb.StringProperty(required=True)
    water_intake = ndb.StringProperty(required=False)
    food_intake = ndb.StringProperty(required=False)
    exercise = ndb.StringProperty(required=False)
    bath = ndb.StringProperty(required=False)

class OtterUser(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
