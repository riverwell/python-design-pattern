#!/usr/bin/env python
# coding: utf-8

from factory.factory import Factory
from listfactory.list_link import ListLink
from listfactory.list_page import ListPage
from listfactory.list_tray import ListTray


class ListFactory(Factory):
    def create_link(self, caption: str, url: str):
        return ListLink(caption, url)

    def create_tray(self, caption: str):
        return ListTray(caption)

    def create_page(self, title: str, author: str):
        return ListPage(title, author)
