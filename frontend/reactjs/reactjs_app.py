#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (Flask, request, current_app, g, make_response,
                   redirect, abort, render_template, jsonify)
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app_ctx = app.app_context()
app_ctx.push()

print("Current App: ", current_app.name)


@app.route("/")
def index_handler():
    print("Vue App")
    return render_template("base.html")


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()

