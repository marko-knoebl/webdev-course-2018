#!/usr/bin/env python
import os
import jinja2
import webapp2
from google.appengine.api import urlfetch
import json

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
        return self.render_template("main.html")

class WeatherHandler(BaseHandler):
    def get(self):
        city = self.request.get('city')
        base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=9d3ae54b4b75a62bd73707396325726e&units=metric&q='
        url = base_url + city
        weather_response = urlfetch.fetch(url)
        weather_data = json.loads(weather_response.content)
        temp = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['main']
        return self.render_template(
            "weather.html",
            {'city': city, 'temp': temp, 'weather_description': weather_description}
        )

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/weather', WeatherHandler)
], debug=True)
