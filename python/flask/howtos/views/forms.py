#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of managing forms.

Taking input from forms
"""

from flask import Blueprint, render_template, request, jsonify

forms = Blueprint('forms', __name__,
                 template_folder="templates", static_folder="static")


@forms.route("/", methods=["GET", "POST"])
def index():
    print "Request method: ", request.method
    print "Request.form: ", request.form
    obj = {}
    if request.method == "POST":
        obj['email'] = request.form['email']

    return render_template('forms.html',
                            obj=obj)

@forms.route("/formhandle", methods=["GET", "POST"])
def formHandler():
    obj = {}
    print "Form handler. reqeust method: ", request.method
    return jsonify(obj)
    
