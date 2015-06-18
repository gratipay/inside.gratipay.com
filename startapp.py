#!/usr/bin/env python
"""
The main script to start website for development,
which also exports WSGI application for production.
"""

from aspen.website import Website

# by WSGI convention, we need to create webapp object
# and by default most WSGI servers look for 'application'
application = Website([])

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    make_server('', 8000, application).serve_forever()
