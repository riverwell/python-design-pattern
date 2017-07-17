#!/usr/bin/env python
# coding: utf-8

from builder import Builder


class Director():
    def __init__(self, builder: Builder):
        self.__builder = builder

    def construct(self):
        self.__builder.make_title("Greeting")
        self.__builder.make_string("朝から昼にかけて")
        self.__builder.make_items(["おはようございます．", "こんにちは．"])
        self.__builder.make_string("夜に")
        self.__builder.make_items(["こんばんは．","おやすみなさい．","さようなら．"])
        self.__builder.close()
