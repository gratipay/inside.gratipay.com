import commands
import os
from collections import namedtuple
from os.path import basename, dirname, join, realpath, isdir

import aspen.execution
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


# Set website.versions.
# =====================

def get_www_gittip_com_version():
    version_file = join(website.repo_root, 'www.gittip.com', 'www', 'version.txt')
    aspen.execution.extras.add(version_file)
    version = open(version_file).read().strip()
    if version.endswith('-dev'):
        version = version[:-len('-dev')]
    return version

website.versions = namedtuple('Versions', 'www_gittip_com gttp_co Gittip_Everywhere ours'.split())
website.versions.ours = commands.getoutput('git rev-parse HEAD')
website.versions.www_gittip_com = get_www_gittip_com_version()


# Set random thing that we're not really using.
# =============================================

website.compress_assets = True
