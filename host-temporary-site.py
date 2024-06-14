#!/usr/bin/env python3

import argparse
import functools
import http.server
import os
import socketserver
import subprocess

# Set the directory containing the files you want to serve
directory = "./placeholder"

# Set the port number for the web server
# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-p", "--port", type=int, default=8000, help="Port number for the web server"
)
args = parser.parse_args()

# Set the port number for the web server
port = args.port


# Create a handler to serve the files
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # If the requested file doesn't exist, serve index.html instead
        if not os.path.exists(self.translate_path(self.path)):
            self.path = "/index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler = functools.partial(MyHandler, directory=directory)

# Close any existing process using the specified port


def close_process_using_port(port):
    try:
        subprocess.run(
            ["lsof", "-ti", f":{port}", "-sTCP:LISTEN", "-n"],
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        pid = e.stdout.decode().strip()
        subprocess.run(["kill", pid])


# Close any existing process using the specified port
close_process_using_port(port)


# Start the web server
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Server started on port {port}")
    httpd.serve_forever()
