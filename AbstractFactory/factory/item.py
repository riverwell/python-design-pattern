#!/usr/bin/env python
# coding: utf-8

from abc import abstractmethod, ABCMeta


class Item(metaclass=ABCMeta):
    def __init__(self, caption):
        self.caption = caption

    @abstractmethod
    def make_html(self) -> str:
        pass
