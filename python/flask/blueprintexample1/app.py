#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from views.home import home
from views.profile import profile


app = Flask(__name__)
app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(profile, url_prefix="/profile")


def main():
    app.run(debug=True, port=5001)

if __name__ == '__main__':
    main()
