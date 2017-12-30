#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask import request
from flask import jsonify
from flask import session
from flask import g

#from flask import abort
#from flask import url_for
from flask import render_template
#from flask import current_app
#from flask import flash
#from flask import make_response
#import json
#import hashlib
#import quotes
import random
import app_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello from the secret world of Flask! ;)'


@app.route("/example1")
def example1():
    print "Index invoked"
    print request


    status = {}
    status['key1'] = "Test key"
    status['key2'] = "test key 2"

    if request.mimetype == "application/json":
        return jsonify(status)
    return (render_template('example1.html'))


@app.route("/example2")
def example2():
    print "Index invoked"
    print request


    status = {}
    status['key1'] = "Test key"
    status['key2'] = "test key 2"

    if request.mimetype == "application/json":
        return jsonify(status)
    return (render_template('example2.html'))


@app.route("/example3")
def example3():
    print "Index invoked"
    print request


    status = {}
    status['key1'] = "Test key"
    status['key2'] = "test key 2"

    if request.mimetype == "application/json":
        return jsonify(status)
    return (render_template('example3.html'))


@app.route("/example4")
def example4():
    print "Index invoked"
    print request


    status = {}
    status['key1'] = "Test key"
    status['key2'] = "test key 2"

    if request.mimetype == "application/json":
        return jsonify(status)
    return (render_template('example4.html'))

@app.route("/example5")
def example5():
    print "Index invoked"
    print request


    status = {}
    status['key1'] = "Test key"
    status['key2'] = "test key 2"

    if request.mimetype == "application/json":
        return jsonify(status)
    return (render_template('example5.html'))

@app.route("/example6")
def example6():
    print "Index invoked"
    print request


    status = {}
    status['key1'] = "Test key"
    status['key2'] = "test key 2"

    if request.mimetype == "application/json":
        return jsonify(status)
    return (render_template('example6.html'))


@app.route("/example7")
def example7():
    print "Index invoked"
    print request


    status = {}
    status['key1'] = "Test key"
    status['key2'] = "test key 2"

    if request.mimetype == "application/json":
        return jsonify(status)
    return (render_template('example7.html'))


@app.route("/rundeckstat", methods=["GET", "POST"])
def handle_rundeckstat():
    print "Rundeck stat. req: %s, args: %s data: %s , conttype: %s" % \
        (request, request.args, request.data, request.content_type)

    if request.method == 'POST':
        print "POST REQUEST"
        data = {}
        data['data'] = int(request.args.get('stat', 0))
        app_session.set_data('rundeckstat', data['data'])
        print "DATA: ", data
    else:
        print "GET REQUEST"
        data = app_session.get_data('rundeckstat')
        print "DATA get: ", data
 
    status = {}
    random_obj = random.Random()
    status['metric_value'] = data['data'] 

    if request.mimetype == "application/json":
        return jsonify(status)
    else:
        return jsonify(status);


@app.route("/generatetoken/<account>/<role>")
def generate_token(account, role):
    print "Generate Token Invoked"
    status = {}
    random_obj = random.Random()
    status['metric_value'] = random_obj.randrange(0, 100)
    if request.mimetype == "application/json":
        return jsonify(status)
    else:
        return jsonify(status);



def main():
    app.run(host='0.0.0.0', port=5001, debug=True)

if __name__ == '__main__':
    main()
