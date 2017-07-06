#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod


class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()
