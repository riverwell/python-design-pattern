#!/usr/bin/env python
# coding: utf-8

from factory.link import Link
from factory.tray import Tray


class ListTray(Tray):
    def __init__(self, caption: str):
        super().__init__(caption)

    def make_html(self):
        buffer = []
        buffer.append("<li>\n")
        buffer.append(self.caption + "\n")
        buffer.append("<ul>\n")
        for t in self.tray:
            buffer.append(t.make_html())
        buffer.append("<ul>\n")
        buffer.append("<li>\n")
        return "".join(buffer)
