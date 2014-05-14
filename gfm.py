from __future__ import absolute_import, division, print_function, unicode_literals

import misaka
from aspen_jinja2_renderer import Renderer as Jinja2Renderer, Factory as Jinja2Factory


def gfm(md):
    html = misaka.html( md
                      , misaka.EXT_STRIKETHROUGH | misaka.EXT_AUTOLINK | misaka.EXT_FENCED_CODE
                      , misaka.HTML_SMARTYPANTS | misaka.HTML_TOC
                       )
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
