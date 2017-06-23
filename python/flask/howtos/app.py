#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from views.home import home
from views.dialogs import dialog


app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(dialog, url_prefix="/dialog")


def main():
    app.run(debug=True, port=5001)

if __name__ == '__main__':
    main()
