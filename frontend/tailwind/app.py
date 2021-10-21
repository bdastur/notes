#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Guardrails Server:
-----------------
"""


from flask import Flask, render_template, jsonify


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("main.html")


@app.route("/app")
def appHandler():
    return render_template("test_app.html")



def main():
    """Main Application"""
    app.run(host="0.0.0.0", port=5003, debug=True)


if __name__ == '__main__':
    main()
