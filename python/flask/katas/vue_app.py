#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (Flask, request, current_app, g, make_response,
                   redirect, abort, render_template)


app = Flask(__name__)
app_ctx = app.app_context()
app_ctx.push()

print("Current App: ", current_app.name)


@app.route("/", methods=["GET"])
def index_handler():
    print("Vue App")

    return render_template("vue_base.html")


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()

