import os
import string
import random
from os.path import basename, dirname, join, realpath, isdir

from aspen import Response
import canonizer
import gfm
from nav import NavItem


# Manually register markdown renderer to work around Heroku deployment woes.
website.renderer_factories['markdown'] = gfm.Factory(website)
website.renderer_factories['jinja2'].Renderer.global_context = {
    'range': range,
    'unicode': unicode,
    'enumerate': enumerate,
    'len': len,
    'float': float,
    'type': type,
    'str': str,
}

website.renderer_default = "markdown"


def add_nav_to_website(website):
    website.nav = NavItem(website, None, website.www_root, '')

def add_nav_current_to_context(dispatch_result, website):
    path = dispatch_result.match
    if basename(path) in website.indices:
        path = dirname(path)
    return {'nav_current': website.nav.by_fs.get(path, website.nav)}

def add_nav_next_to_context(nav_current, website):
    return {'nav_next': nav_current.next_child}

def only_allow_certain_methods(request):
    whitelisted = ['GET', 'HEAD', 'POST']
    if request.method.upper() not in whitelisted:
        raise Response(405)

website.algorithm.insert_before('dispatch_request_to_filesystem', only_allow_certain_methods)
website.algorithm.insert_after('dispatch_request_to_filesystem', add_nav_to_website)
website.algorithm.insert_after('add_nav_to_website', add_nav_current_to_context)
website.algorithm.insert_after('add_nav_current_to_context', add_nav_next_to_context)


# Hostname canonicalization
# =========================

canonize = canonizer.Canonizer(os.environ.get('CANONICAL_LOCATION', ''))
website.algorithm.insert_after('parse_environ_into_request', canonize)


# Set website.version.
# ====================
# Yeesh, what a hack. At Heroku we don't have a git repo once deployed, so
# instead of using a git SHA we're going to just use a random string. Doing
# this "right" would mean storing the real version SHA somewhere during
# deployment.

website.version = ''.join([random.choice(string.letters) for i in range(32)])


# Set random thing that we're not really using.
# =============================================

website.compress_assets = False # If set to True, the responsiveness on the lower
                                # homepage breaks. :-/
