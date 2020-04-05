#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import (Flask, request, jsonify, session, render_template)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello from the secret world of Flask! ;)'


@app.route("/")
def handle_sample_1():
    print("Sample Invoked")
    return (render_template('sample_1.html'))

@app.route("/2")
def handle_sample_2():
    print("Sample 2 invoked")
    return (render_template('sample_2.html'))

@app.route("/css1")
def handle_css1():
    print("Css Example 1")
    return(render_template("css_example_1.html"))

@app.route("/css2")
def handle_css2():
    print("CSS Example 2")
    return(render_template("position.html"))

@app.route("/project")
def handle_project():
    print("Main project")
    return(render_template("project.html"))

@app.route("/packages")
def handle_packages():
    print("Packagesproject")
    return(render_template("packages.html"))

@app.route("/customers")
def handle_customers():
    print("Customers page")
    return(render_template("customers.html"))
                                              


def main():
    app.run(host='127.0.0.1', port=5003, debug=True)

if __name__ == '__main__':
    main()

