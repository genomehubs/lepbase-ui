#!/usr/bin/env python3

import functools
import http.server
import socketserver

# Set the directory containing the files you want to serve
directory = "./placeholder"

# Set the port number for the web server
port = 8000

# Create a handler to serve the files
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=directory)

# Start the web server
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Server started on port {port}")
    httpd.serve_forever()
