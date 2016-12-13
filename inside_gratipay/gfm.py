from __future__ import absolute_import, division, print_function, unicode_literals

import mistune
from mistune_contrib.toc import TocMixin
from aspen_jinja2_renderer import Renderer as Jinja2Renderer, Factory as Jinja2Factory


# setup Markdown rendering, with anchors for headers
class TocRenderer(TocMixin, mistune.Renderer):
    pass
toc = TocRenderer()
markdown = mistune.Markdown(renderer=toc)


def gfm(md):
    toc.reset_toc()
    html = markdown( md )
    return html


wrapper = """
{{% extends "templates/page.html" %}}
{{% block content %}}
{}
{{% endblock %}}
"""

class Renderer(Jinja2Renderer):
    def compile(self, filepath, raw):
        raw = wrapper.format(gfm(raw))
        return Jinja2Renderer.compile(self, filepath, raw)


class Factory(Jinja2Factory):
    Renderer = Renderer
