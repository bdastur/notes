#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from views.home import home


app = Flask(__name__)
app.register_blueprint(home)
