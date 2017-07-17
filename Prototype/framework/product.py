#!/usr/bin/env python
# coding: utf-8

from zope.interface import Interface
from abc import abstractmethod


class Product(Interface):
    @abstractmethod
    def use(self, s: str):
        pass

    @abstractmethod
    def create_clone(self)->'Product':
        pass
