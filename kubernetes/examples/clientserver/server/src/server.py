#!/usr/bin/env python

import http.server
import socketserver


def main():
    serverPort = 8000
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", serverPort), handler) as httpd:
        httpd.serve_forever()


if __name__ == '__main__':
    main()
