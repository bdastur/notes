#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import (Flask, request, jsonify, session, render_template)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello from the secret world of Flask! ;)'


@app.route("/")
def handle_index():
    print("Sample Invoked")
    return (render_template('index.html'))

@app.route("/credentials")
def handle_credentials():
    print("Get Credentials");


    creds = {
        'access_key_id': "ASIxxxxxxx6UH",
        'secret_access_key': "zkFI5VOQ",
        'session_token': "Fwxxxxxxx"
    }

    return jsonify(creds)


def main():
    app.run(host='127.0.0.1', port=5001, debug=True)

if __name__ == '__main__':
    main()

