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
def example1():
    print "Index invoked"
    print request


    status = {}
    status['key1'] = "Test key"
    status['key2'] = "test key 2"

    if request.mimetype == "application/json":
        return jsonify(status)
    return (render_template('bootstrap_starter.html'))



def main():
    app.run(host='127.0.0.1', port=5001, debug=True)

if __name__ == '__main__':
    main()

