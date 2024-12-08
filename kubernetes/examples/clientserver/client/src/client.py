#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import http.client


def main():
    serverPort = 8000
    serverAddress = "simpleserverservice"
    connection = http.client.HTTPConnection(serverAddress, serverPort, timeout=10)

    while True:
        connection.request("GET", "/")
        response = connection.getresponse()
        status = response.status
        reason = response.reason
        data = response.read()
        print("Status: %s, Reason: %s" % (status, reason))
        print("Data: ", data)
        
        time.sleep(2)
        print("Continue.")



if __name__ == '__main__':
    main()

