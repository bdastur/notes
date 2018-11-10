#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import (Flask, render_template, g)
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app_ctx = app.app_context()
app_ctx.push()

dbPath = "sqlite:///" + os.path.join("/tmp", "data.sqlite")
app.config['SQLALCHEMY_DATABASE_URI'] = dbPath
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class DBHandler(object):
    def __init__(self):
        if 'db' not in g:
            print "G.DB set"
            g.db = 'test'

        if 'dbInitiated' not in g:
            print "Initialize DB!"
            g.dbInitiated = True
            db.create_all()

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/", methods=["GET"])
def index_handler():
    DBHandler()
    print "G.DB: ", g.db
    return "Hello DB"





def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
