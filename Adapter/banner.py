#!/usr/bin/env python
# coding: utf-8


class Banner:
    def __init__(self, string):
        self.__string = string

    def show_with_paren(self):
        print("(" + self.__string + ")")

    def show_with_aster(self):
        print("*" + self.__string + "*")
