#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
- Simple Rendering with a dict
'''

from flask import (Flask, request, render_template)

app = Flask(__name__)


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
        self.user_agent = request.headers.get('User-Agent')

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def getRequestUserAgent(self):
        return self.user_agent



@app.route("/newuser/<name>", methods=["GET"])
def newuser_handler(name):
    print "New User"
    newobj = MyObj(request)
    newobj.set_name(name)
    return render_template("newuser.html", data=newobj)



def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
