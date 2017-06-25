#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Example of managing forms.
Taking input from forms
'''

from flask import Blueprint, render_template, request

forms = Blueprint('forms', __name__,
                 template_folder="templates", static_folder="static")


@forms.route("/", methods=["GET", "POST"])
def index():
    print "Request method: ", request.method
    print "Request.form: ", request.form
    
    return render_template('forms.html')
