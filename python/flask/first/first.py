#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello Flask!</h1>'

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello %s</h1>" % name


def main():
    app.run(port=5001, debug=True)

if __name__ == '__main__':
    main()
