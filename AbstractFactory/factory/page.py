#!/usr/bin/env python
# coding: utf-8

from abc import abstractmethod, ABCMeta
from factory.item import Item


class Page(metaclass=ABCMeta):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.content = []

    def add(self, item: Item):
        self.content.append(item)

    def output(self):
        filename = self.title + ".html"
        try:
            with open(filename, "w") as f:
                f.write(self.make_html())
            print(filename + "を作成しました．")
        except IOError:
            print(filename + "の作成に失敗しました．")

    @abstractmethod
    def make_html(self) -> str:
        pass
