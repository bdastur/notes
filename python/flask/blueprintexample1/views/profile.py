#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

profile = Blueprint('profile', __name__,
                    template_folder="templates",
                    static_folder="static")

@profile.route("/")
def profileindex():
    return "Hello Profile index"

@profile.route("/account/<username>")
def account(username):
    print "username: ", username
    return "<h1>Username is: %s</h1>" % username, 200

    
