#!/usr/bin/env python
# coding: utf-8

from abc import abstractmethod, ABCMeta
from factory.item import Item


class Link(Item, metaclass=ABCMeta):
    def __init__(self, caption: str, url: str):
        super().__init__(caption)
        self.url = url
