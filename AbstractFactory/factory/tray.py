#!/usr/bin/env python
# coding: utf-8

from abc import abstractmethod, ABCMeta
from factory.item import Item


class Tray(Item, metaclass=ABCMeta):
    def __init__(self, caption: str):
        super().__init__(caption)
        self.tray = []

    def add(self, item: Item):
        self.tray.append(item)
