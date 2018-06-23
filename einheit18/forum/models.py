from google.appengine.ext import ndb

class Message(ndb.Model):
    title = ndb.StringProperty()
    message_text = ndb.StringProperty()