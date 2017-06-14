#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

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
