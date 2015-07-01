#!/usr/bin/env python
"""
The main script to start website for development,
which also exports WSGI application for production.
"""
 
HOST = ''    # by default run on all interfaces
PORT = 8537  # default/devserver port
 
import sys
from aspen.website import Website
 
aspen_config = [
    '--www_root=www/',
    '--project_root=.'
]
 
for param in sys.argv:
    if param.startswith('--port'):
        _, PORT = param.split('=')
 
 
# by WSGI convention, we need to create webapp object
# and by default most WSGI servers look for 'application'
application = Website(aspen_config)
 
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("* Running development server on http://%s:%s" % (HOST, PORT))
    make_server(HOST, PORT, application).serve_forever()
 
