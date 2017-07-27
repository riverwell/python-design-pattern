#!/usr/bin/env python
# coding: utf-8

from zope.interface import Interface
from abc import abstractmethod, ABCMeta


class Strategy(Interface):
    @abstractmethod
    def next_hand(self):
        pass

    @abstractmethod
    def study(self, win: bool):
        pass
