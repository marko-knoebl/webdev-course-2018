#!/usr/bin/env python
import os
import jinja2
import webapp2

from google.appengine.api import users

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
        user = users.get_current_user()

        if user == None:
            # benutzer nicht eingeloggt
            login_url = users.create_login_url('/forum')
            return self.render_template(
                'forum.html',
                {
                    'logged_in': False,
                    'login_url': login_url
                }
            )
        else:

            nickname = user.nickname()
            messages = Message.query().fetch()
            logout_url = users.create_logout_url('/forum')

            return self.render_template(
                'forum.html',
                {
                    'logged_in': True,
                    'nickname': nickname,
                    'logout_url': logout_url,
                    'user': user,
                    'messages': messages
                }
            )

class MessageDetailsHandler(BaseHandler):
    def get(self, message_id):
        # hol den Eintrag mit der angegegebenen id aus der Dataenbank
        message = Message.get_by_id(int(message_id))

        return self.render_template('message-details.html',
                                    {'message': message})


class AddPostHandler(BaseHandler):
    def get(self):
        return self.render_template('add-post.html')

class AddPostResultHandler(BaseHandler):
    def post(self):
        title = self.request.get('title')
        message1 = self.request.get('message')

        message_db_entry = Message(title=title, message_text=message1)
        message_db_entry.put()

        return self.render_template('add-post-result.html',
                                    {'new_post_title': title})

class EditHandler(BaseHandler):
    def post(self, message_id):
        # hole den 'new-text'- Parameter aus der HTTP-Anfrage
        new_text = self.request.get('new-text')

        # hole den Datenbankeintrag zur Message
        message = Message.get_by_id(int(message_id))

        # aendere den Datenbankeintrag um
        message.message_text = new_text

        # speichere den geaenderten Datenbankeintrag
        message.put()

        return self.render_template('edit.html')

class DeleteHandler(BaseHandler):
    def post(self, message_id):

        # hole den Datenbankeintrag zur Message
        message = Message.get_by_id(int(message_id))

        # loesche den Datenbankeintrag
        message.key.delete()

        return self.render_template('delete.html')


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/forum', ForumHandler, name='forum'),
    webapp2.Route('/add-post', AddPostHandler),
    webapp2.Route('/add-post-result', AddPostResultHandler),
    # lies am ende der Route einen Parameter aus, der aus
    # einer oder mehreren Ziffern besteht ( \d+ )
    # und weise ihm den namen message_id zu
    webapp2.Route('/message/<message_id:\d+>', MessageDetailsHandler),
    webapp2.Route('/edit/<message_id:\d+>', EditHandler),
    webapp2.Route('/delete/<message_id:\d+>', DeleteHandler)
], debug=True)
