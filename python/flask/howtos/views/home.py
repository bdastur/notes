#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

home = Blueprint('home', __name__,
                 template_folder="templates", static_folder="static")


@home.route("/")
def index():
    return render_template('home.html')
