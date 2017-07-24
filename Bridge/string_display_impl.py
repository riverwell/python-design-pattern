#!/usr/bin/env python
# coding: utf-8

from display_impl import DisplayImpl

class StringDisplayImpl(DisplayImpl):
    def __init__(self, string: str):
        self.__string = string
        self.__width = len(string.encode("utf-8"))

    def raw_open(self):
        self.__printline()

    def raw_print(self):
        print("|{}|".format(self.__string))

    def raw_close(self):
        self.__printline()

    def __printline(self):
        print('+', end='')
        for i in range(self.__width):
            print('-', end='')
        print('+')
