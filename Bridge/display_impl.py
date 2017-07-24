#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod


class DisplayImpl(metaclass=ABCMeta):
    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_print(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass
