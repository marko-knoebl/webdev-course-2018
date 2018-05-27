#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Message


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):

        messages = Message.query().fetch()
        return self.render_template(
            "hello.html",
            params={'messages': messages}
        )

class AddHandler(BaseHandler):
    def get(self):
        return self.render_template('add-message.html')

class PostHandler(BaseHandler):
    def post(self):
        # lies den request-parameter 'message' aus
        # und speichere ihn unter der Python-Variable 'message'
        message = self.request.get("message")

        # speichere die message in der Datenbank
        msg = Message(message_text=message)
        msg.put()

        return self.render_template(
            'post.html',
            # uebergib die message-Variable an Jinja
            params = {'message': message}
        )

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/home', MainHandler),
    webapp2.Route('/add-message', AddHandler),
    webapp2.Route('/post', PostHandler),
], debug=True)
