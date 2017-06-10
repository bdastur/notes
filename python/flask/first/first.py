#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask import make_response
from flask import redirect, abort

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello Flask!</h1>'

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello %s</h1>" % name

@app.route('/cookie/')
def setcookie():
    response = make_response(
    '<h1>Set Cookie</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirectme')
def redirect_test():
    return redirect('/')


@app.route('/abortonodd/<number>')
def abort_test(number):
    if int(number) % 2 != 0:
        abort(500)
    return '<h2>Numer %s is even</h2>' % number


def main():
    app.run(port=5001, debug=True)

if __name__ == '__main__':
    main()
