#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
- Flask forms
- Cross-site Request Forgery (CSRF) Protection
- url_for() to generate urls.
- flash() for message flashing
'''

from flask import (Flask, render_template, flash,
                   redirect, url_for, session )
from flask_wtf import Form
from flask_wtf import FlaskForm
import wtforms
import wtforms.validators as validators
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = ''.join(
    random.choice(string.ascii_letters + string.digits) for _ in range(20))


class NameForm(FlaskForm):
    name = wtforms.StringField('Name', validators=[validators.Required()])
    submit = wtforms.SubmitField('Submit')


@app.route("/form", methods=["GET", "POST"])
def form_handler():
    print "Form handler"
    form = NameForm()
    if form.name.data is not None:
        print "Set session to %s" % form.name.data
        if form.name.data != "Behzad Dastur":
            print "Flash %s" % form.name.data
            flash('Looks like you are here')

        session['name'] = form.name.data
        return redirect(url_for("user_handler", name=form.name.data))
    else:
        print "Validate on submit failed"

    name = form.name.data
    print "NAME: ", name
    form.name.data = ""
    return render_template('form1.html', form=form, name=name)

@app.route("/user/<name>", methods=["GET"])
def user_handler(name):
    print "User handler!", session['name']
    return render_template('form_user.html', name=name)


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
