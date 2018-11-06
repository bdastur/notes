#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
- Simple Rendering with a dict
- Rendering from an object
- Jinja2 filters, macros
- Jinja2 template inheritance
- Error handlers
- Localization of dates and times with flask-moment
'''

from flask import (Flask, request, render_template)
from flask_moment import Moment
import datetime


app = Flask(__name__)
moment = Moment(app)

now = datetime.datetime.utcnow()

#########################################
# Simple Rendering
##########################################

@app.route("/user/<name>", methods=["GET"])
def index_handler(name):
    print "Index!"
    data = {}
    data['name'] = name
    data['user_agent'] = request.headers.get('User-Agent')
    return render_template("index.html", data=data)


#########################################
# Rendering from an object.
##########################################

class MyObj(object):
    def __init__(self, request):
        self.attributes = {}
        self.user_agent = request.headers.get('User-Agent')

    def set_name(self, name):
        self.name = name

    def set_attributes(self, name):
        self.attributes = {
            name: {
                'age': 41,
                'height': 156,
                'location': "Fremont, California",
                'married': True
            }
        }

    def set_utc_time(self):
        self.utctime = datetime.datetime.utcnow()

    def get_utc_time(self):
        return self.utctime

    def get_name(self):
        return self.name

    def get_attributes(self, name):
        return self.attributes[name]

    def getRequestUserAgent(self):
        return self.user_agent



@app.route("/newuser/<name>", methods=["GET"])
def newuser_handler(name):
    print "New User"
    newobj = MyObj(request)
    newobj.set_name(name)
    newobj.set_attributes(name)
    newobj.set_utc_time()
    return render_template("newuser.html", data=newobj)


################################################
# Error handlers.
################################################
@app.errorhandler(404)
def page_not_found(e):
    return "Page not found!"


################################################
# J2 template inheritance
################################################
@app.route("/base")
def inherit_handler():
    return render_template('head.html')


################################################
# Localication of dates and times with flask-moment
# Server needs uniform time units that are independent of the location of
# each user, so a typically coordinated UTC is used. For users however
# seeing times expressed in UTC can be confusing, as a user always
# expect to see dates and times presented in local time.
# A solution that allows the server to work exclusively in UTC is to
# send these time units to the web browser, where they can be converted
# to local time and rendered.
################################################
@app.route("/moment")
def moment_handler():
    now = datetime.datetime.utcnow()
    data = {}
    data['name'] = "Behzad"
    data['now'] = now
    return render_template('head.html', data=data)



def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
