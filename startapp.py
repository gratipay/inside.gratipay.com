#!/usr/bin/env python
"""The main script to start the website.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import os
from wsgiref.simple_server import make_server

from aspen.website import Website


# by WSGI convention, we need to create webapp object
# and by default most WSGI servers look for 'application'
application = Website(['--www_root=www/', '--project_root=.'])


def serve(application):
    host = ''  # run on all interfaces
    port = int(os.environ.get('PORT', 8536))
    print("* Running development server on http://%s:%s" % (host, port))
    make_server(host, port, application).serve_forever()


if __name__ == '__main__':
    serve(application)
