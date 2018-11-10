#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (Flask, render_template)


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("bs1.html")

@app.route("/jumbotron", methods=["GET"])
def jumbotron():
    return render_template("jumbotron.html")

@app.route("/buttons", methods=["GET"])
def buttons():
    return render_template("buttons.html")

def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
