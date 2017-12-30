#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import shelve
import datetime
import string
import random     

APP_SESSION_PATH = "/tmp"

def set_data(metric_name, value):
    now = datetime.datetime.now()

    filename = metric_name.lower()
    filepath = os.path.join(APP_SESSION_PATH, filename)

    print "Shelve session data ", filepath

    d = shelve.open(filepath)
    d['timestamp'] = now
    d['metric_name'] = metric_name
    d['data'] = value 
    d.close()


def get_data(metric_name):
    print "APP SESSION, GET DATA"
    app_session_data = {}

    filename = metric_name.lower()
    filepath = os.path.join(APP_SESSION_PATH, filename)

    d = shelve.open(filepath)
    if d:
        app_session_data['data'] = d['data']
        app_session_data['timestamp'] = d['timestamp']
        d.close()
        app_session_data['curtime'] = datetime.datetime.now()
    else:
        app_session_data['data'] = 0
        app_session_data['curtime'] = datetime.datetime.now()
        app_session_data['timestamp'] = datetime.datetime.now()

    return app_session_data

 
