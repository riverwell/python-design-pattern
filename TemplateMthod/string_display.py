#!/usr/bin/env python
# coding: utf-8

from abstract_display import AbstractDisplay


class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.__string = string
        # バイト列での長さを取得(ユニコードだと日本語1文字3バイトなので，長くなりすぎるが)
        self.__width = len(string.encode("utf-8"))

    def open(self):
        self.__print_line()

    def print(self):
        print("|" + self.__string + "|")

    def close(self):
        self.__print_line()

    def __print_line(self):
        print("+", end="")
        for i in range(self.__width):
            print("-", end="")
        print("+")
