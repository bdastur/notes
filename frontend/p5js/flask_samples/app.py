#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import (Flask,
                   render_template)
import random


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello from the secret world of Flask! ;)'


@app.route("/")
def handle_index():
    links = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint == "static":
            continue
        links.append((rule.rule, rule.rule))

    return render_template("index.html", links=links)


@app.route("/instance_mode")
def handle_instance_mode():
    return (render_template("instance_mode.html"))


@app.route("/shapes")
def handle_shapes():
    return(render_template("shapes.html"))


@app.route("/custom_shapes")
def handle_custom_shapes():
    return(render_template("custom_shapes.html"))


@app.route("/mouse_moves")
def handle_mouse_moves():
    return(render_template("mouse_moves.html"))


def main():
    app.run(host='127.0.0.1', port=5001, debug=True)

if __name__ == '__main__':
    main()

