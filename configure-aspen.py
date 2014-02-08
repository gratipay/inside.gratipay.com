import commands
import os
import string
import random
from os.path import basename, dirname, join, realpath, isdir

from nav import NavItem


website.renderer_default = "jinja2"
website.renderer_factories['jinja2'].Renderer.global_context = {
    'range': range,
    'unicode': unicode,
    'enumerate': enumerate,
    'len': len,
    'float': float,
    'type': type,
    'str': str,
}


def add_nav_to_website(website):
    website.nav = NavItem(website, None, website.www_root, '')

def add_nav_current_to_context(request, website):
    fs = request.fs
    if basename(request.fs) in website.indices:
        fs = dirname(fs)
    request.context['nav_current'] = website.nav.by_fs.get(fs, website.nav)

add_nav_to_website(website)

website.algorithm.insert_after('dispatch_request_to_filesystem', add_nav_to_website)
website.algorithm.insert_after('dispatch_request_to_filesystem', add_nav_current_to_context)


# Download repos.
# ===============
# We try to take documentation from source code where possible.

repos = [
    'https://github.com/gittip/www.gittip.com.git',
    'https://github.com/gittip/gttp.co.git',
    'https://github.com/gittip/Gittip-Everywhere.git',
]

website.repo_root = realpath(join(website.project_root, 'repos'))

if not isdir(website.repo_root):
    os.system('mkdir {}'.format(website.repo_root))
    for repo in repos:
        os.system('cd {} && git clone {}'.format(website.repo_root, repo))


# Set website.version.
# ====================
# Yeesh, what a hack. At Heroku we don't have a git repo once deployed, so
# instead of using a git SHA we're going to just use a random string. Doing
# this "right" would mean storing the real version SHA somewhere during
# deployment.

website.version = ''.join([random.choice(string.letters) for i in range(32)])


# Set random thing that we're not really using.
# =============================================

website.compress_assets = True
