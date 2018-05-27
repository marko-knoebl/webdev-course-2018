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
        return self.render_template("hello.html")

class ForumHandler(BaseHandler):
    def get(self):
        messages = Message.query().fetch()
        return self.render_template('forum.html', {'messages': messages})

class MessageDetailsHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        return self.render_template('message_details.html',
                                    {'message': message})


class AddPostHandler(BaseHandler):
    def get(self):
        return self.render_template('add-post.html')

class AddPostResultHandler(BaseHandler):
    def post(self):
        title = self.request.get('title')
        message1 = self.request.get('message')

        message_db_entry = Message(title=title, message=message1)
        message_db_entry.put()

        return self.render_template('add-post-result.html',
                                    {'new_post_title': title})

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/forum', ForumHandler),
    webapp2.Route('/add-post', AddPostHandler),
    webapp2.Route('/add-post-result', AddPostResultHandler),
    # lies am ende der Route einen Parameter aus, der aus
    # einer oder mehreren Ziffern besteht ( \d+ )
    # und weise ihm den namen message_id zu
    webapp2.Route('/message/<message_id:\d+>', MessageDetailsHandler)
], debug=True)
