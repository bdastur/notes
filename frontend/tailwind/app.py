#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Guardrails Server:
-----------------
"""


from flask import Flask, render_template, jsonify
import prometheus_client
import grail.awslibs.supportlib as talib


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("main.html")



def main():
    """Main Application"""
    app.run(host="0.0.0.0", port=5003, debug=True)


if __name__ == '__main__':
    main()
