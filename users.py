from google.appengine.ext import ndb

class OtterSetting(ndb.Model):
    water_num_intake = ndb.IntegerProperty(required=True)
    food_intake = ndb.IntegerProperty(required=True)
    food_intake_counter = ndb.IntegerProperty(required=True)
    exercise = ndb.IntegerProperty(required=True)
    bath = ndb.IntegerProperty(required=True)
    owner = ndb.StringProperty(required=True)

class OtterUser(ndb.Model):
    otter_name = ndb.StringProperty()
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
