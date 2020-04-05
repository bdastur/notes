#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask import request
from flask import jsonify
from flask import session
from flask import render_template
import random


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello from the secret world of Flask! ;)'


@app.route("/starter")
def handle_bootstrap_starter():
    print("Index invoked")
    print(request)


    status = {}
    status['key1'] = "Test key"
    status['key2'] = "test key 2"

    if request.mimetype == "application/json":
        return jsonify(status)
    return (render_template('bootstrap_starter.html'))

@app.route("/grids")
def handle_grids():
    print("Grids handler")
    return (render_template('grids.html'))

@app.route("/sample_layout")
def handle_sample_layout():
    print("Sample Layout")
    return(render_template('sample_layout.html'))

@app.route("/test1")
def handle_test():
    return(render_template('accordians.html'))

@app.route("/backbone")
def handle_backbone_example():
    print("Backbone")
    return (render_template('backbone_todo.html'))

def main():
    app.run(host='127.0.0.1', port=5001, debug=True)

if __name__ == '__main__':
    main()

