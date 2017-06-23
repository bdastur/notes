#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from flask import request

home = Blueprint('home', __name__,
                 template_folder="templates",
                 static_folder="static")


@home.route("/")
def homeindex():
    return render_template('home.html')

@home.route("/user/<username>")
def home_username(username):
    print "username: ", username
    return render_template('user.html')

@home.route("/userinput", methods=['POST', 'GET'])
def userinput():
    obj = {}
    obj['method'] = "GET"
    if request.method == "POST":
        print "POST method"
        print "Form info: ", request.form
        print "email: ", request.form['email']
        obj['method'] = "POST"
    else:
        print "GET METHOD"

    return render_template('userinput.html',obj=obj)
