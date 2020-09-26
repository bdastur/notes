#!/usr/bin/env python
# -*- coding: utf-8 -*-


import prometheus_client
from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t, counter):
    """A dummy function that takes some time."""
    counter. inc()
    time.sleep(t)


# A Guage.
def get_cpu_utilization(gauge):
    """A dummy function that returns a random value - showin fake cpu utilization"""
    cpu_util = random.randint(1, 100)
    gauge.set(cpu_util)


# A Historam
def get_request_size(histogram):
    """A dummy function that requests a fake request size - historam"""
    size = random.randint(0, 10)
    size = size * 0.02
    histogram.labels(app_name="firstapp", environment="development").observe(size)

#  Enum
def get_password_policy_info(e):
    """A dummy function that requests  fake check on password policy"""    
    e.labels(account='dev1').state('average')


# Info
def get_account_info(info):
    """ A dummy function that gets some info for account"""
    users = random.randint(20, 200)
    roles = random.randint(4, 44)
    info.labels(account="dev1").info({'users': str(users), 'roles': str(roles), 'sec': 'weak'}) 


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8081)
    # Generate some requests.
    counter = prometheus_client.Counter('count_process_request', 'Count the number of times this API is invoked')
    gauge = prometheus_client.Gauge('cpu_utilization', 'A fake cpu utilization')

    #hist_buckets = (50.0,100.0,150.0,200.0,300.0,500.0,1000.0)
    histogram = prometheus_client.Histogram('request_size_bytes', 
                                            'A fake http request body size in bytes',
                                            ['app_name', 'environment'])

    sec_status = prometheus_client.Enum('password_policy_status', 
                                        'A status on security',
                                        ['account'],
                                        states=["weak", "average", "strong"])

    info = prometheus_client.Info('account_info', 'Some data', ["account"]) 
    while True:
        process_request(random.randint(1, 5), counter)
        get_cpu_utilization(gauge)
        get_request_size(histogram)
        get_password_policy_info(sec_status)
        get_account_info(info)
        time.sleep(5)


