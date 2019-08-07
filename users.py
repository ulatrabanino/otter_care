from google.appengine.ext import ndb

class Otter(ndb.Model):
    water_intake = ndb.DateTimeProperty(required=True)
    water_num_intake = ndb.IntegerProperty(required=True)
    food_intake1 = ndb.DateTimeProperty(required=True)
    food_intake2 = ndb.DateTimeProperty(required=True)
    food_intake3 = ndb.DateTimeProperty(required=True)
    exercise = ndb.DateTimeProperty(required=True)
    bath = ndb.DateTimeProperty(required=True)

class OtterUser(ndb.Model):
    otter_name = ndb.StringProperty()
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
