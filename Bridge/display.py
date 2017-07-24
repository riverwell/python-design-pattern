#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod

from display_impl import DisplayImpl


class Display():
    def __init__(self, impl: DisplayImpl):
        self.__impl = impl

    def open(self):
        self.__impl.raw_open()

    def print(self):
        self.__impl.raw_print()

    def close(self):
        self.__impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()
