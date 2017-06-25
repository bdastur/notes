#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request

dialog = Blueprint('dialog', __name__,
                 template_folder="templates", static_folder="static")


@dialog.route("/")
def index():
    return render_template('dialog.html')


@dialog.route("/test")
def test():
    return render_template('test.html')

    
