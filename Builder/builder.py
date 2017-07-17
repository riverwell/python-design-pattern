#!/usr/bin/env python
# coding: utf-8

from abc import abstractmethod, ABCMeta


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def make_title(self, title: str):
        pass

    @abstractmethod
    def make_string(self, string: str):
        pass

    @abstractmethod
    def make_items(self, items: [str]):
        pass

    @abstractmethod
    def close(self):
        pass
