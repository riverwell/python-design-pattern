#!/usr/bin/env python
# coding: utf-8

from factory.link import Link
from factory.page import Page


class ListPage(Page):
    def __init__(self, title: str, author: str):
        super().__init__(title, author)

    def make_html(self):
        buffer = []
        buffer.append("<html><head><title>{}</title></head>\n".format(self.title))
        buffer.append("<body>\n")
        buffer.append("<h1>{}</h1>".format(self.title))
        buffer.append("<ul>\n")
        for c in self.content:
            buffer.append(c.make_html())
        buffer.append("</ul>\n")
        buffer.append("<hr><address>{}</address>\n".format(self.author))
        buffer.append("</body></html>\n")
        print(buffer)
        return "".join(buffer)
