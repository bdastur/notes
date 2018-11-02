#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (Flask, request, current_app)


app = Flask(__name__)
app_ctx = app.app_context()
app_ctx.push()

print "Current App: ", current_app.name




# Multiple routes can be managed by a single view
# function

@app.route("/", methods=["GET"])
@app.route("/test", methods=["GET"])
def index_handler():
    print "Index Handler!"
    return "Hello Flask!"


# Dynamic routes
@app.route("/user/<name>", methods=["GET"])
def user_get_handler(name):
    print "Name passed: ", name
    return "Hello %s" % name


# When Flask receives a request from a client, it needs to make a
# few objects available to the view function that will handle it
# An example of that is the request object. It encapsulates the HTTP
# request sent by the client.
@app.route("/requestobj")
def requestobj_test_handler():
    user_agent = request.headers.get('User-Agent')
    print "headers: ", request.headers.keys()
    return "User agent: %s" % user_agent


# You can create new URL maps using the add_url_rule(), just
# like you use the app.route() decorator.
app.add_url_rule('/newrule', 'index', index_handler)



def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
