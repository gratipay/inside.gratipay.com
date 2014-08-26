"""Navigation aides for Inside Gratipay.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from collections import OrderedDict
from os.path import join, realpath, isfile, isdir, basename

from aspen import resources
from aspen.http.request import Request
from aspen.resources.static_resource import StaticResource


def get_simplate_context(website, fs):
    request = Request()
    request.fs = fs
    request.website = website
    resource = resources.get(request)
    return {} if isinstance(resource, StaticResource) else resource.pages[0]


class NavItem(OrderedDict):

    by_fs = {}  # intentionally class-global
    by_url = {}

    def __init__(self, website, parent, fs, slug):
        OrderedDict.__init__(self)
        self.parent = parent
        self.fs = fs
        self.filename = basename(fs)
        self.url = '/' if parent is None else \
                   '/'.join([parent.url if parent.url != '/' else '', slug])

        self.by_fs[fs] = self
        self.by_url[self.url] = self

        self.slug = slug
        self.isdir = isdir(fs)

        if self.isdir:
            simplate = self.find_index(website.indices, fs)
        elif fs.endswith('.spt'):
            simplate = fs
        else:
            simplate = None

        context = {}
        if simplate is not None:
            context = get_simplate_context(website, simplate)
            slugs = context.get('nav_children', [])
            for slug in slugs:
                new_fs = join(fs, slug)
                if not isdir(new_fs):
                    new_fs += '.spt'
                child = NavItem(website, self, new_fs, slug)
                self[child.slug] = child  # Populate self as an OrderedDict

        self.title = context.get('nav_title', '[Untitled]')


    def __str__(self):
        return '<NavItem: {}>'.format(self.url)
    __repr__ = __str__


    @property
    def next_child(self):
        next = None
        parent = self.parent
        if parent is not None:
            siblings = parent.children
            for i, child in enumerate(siblings):
                if child is self:
                    break
            if i+1 < len(siblings):
                next = siblings[i+1]
        return next


    @property
    def children(self):
        return self.values()


    @property
    def discuss_url(self):
        tmpl = 'https://github.com/gratipay/inside.gratipay.com/issues/new?title=feedback on {}'
        return tmpl.format(self.title)

    @property
    def edit_url(self):
        tmpl = 'https://github.com/gratipay/inside.gratipay.com/edit/master/www{}.spt'
        return tmpl.format(self._github_snip)

    @property
    def history_url(self):
        tmpl = 'https://github.com/gratipay/inside.gratipay.com/commits/master/www{}.spt'
        return tmpl.format(self._github_snip)

    @property
    def _github_snip(self):
        github_snip = self.url
        if self.isdir:
            github_snip += '/index'
        return github_snip

    def find_index(self, indices, fs):
        for name in indices:
            candidate = realpath(join(fs, name))
            if isfile(candidate):
                return candidate
        return fs
