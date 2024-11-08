#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (Flask, request, current_app, g, make_response,
                   redirect, abort, render_template, jsonify)


app = Flask(__name__)
app_ctx = app.app_context()
app_ctx.push()

print("Current App: ", current_app.name)


@app.route("/", methods=["GET"])
def index_handler():
    print("Vue App")
    return render_template("vue_base.html")


@app.route("/users", methods=["GET"])
def get_users_handler():
    print("Get Users")
    users = { 
        "jack": {
            "age": 4
        },
        "jake":{
            "age": 43
        }
    }
    return(jsonify(users))


@app.route("/components", methods=["GET"])
def components_handler():
    print("Components")
    return render_template("vue_component.html")


@app.route("/charts", methods=["GET"])
def charts_handler():
    print("Charts")
    return render_template("charts_example.html")


@app.route("/costs", methods=["GET"])
def get_costs_handler():
    print("Get Users")
    cost = [32, 23, 21, 10, 9, 55]
    return(jsonify(cost))




def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()

