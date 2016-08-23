#!/usr/bin/env python
"""
The main script to start website for development,
which also exports WSGI application for production.
"""

HOST = ''    # by default run on all interfaces
PORT = 8536  # default/devserver port

import sys

for param in sys.argv:
    if param.startswith('--port'):
        _, PORT = param.split('=')
        PORT = int(PORT)


# by WSGI convention, we need to create webapp object
# and by default most WSGI servers look for 'application'
from inside_gratipay import website as application

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("* Running development server on http://%s:%s" % (HOST or 'localhost', PORT))
    make_server(HOST, PORT, application).serve_forever()
