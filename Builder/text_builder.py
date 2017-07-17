#!/usr/bin/env python
# coding: utf-8

from builder import Builder


class TextBuilder(Builder):
    def __init__(self):
        # str型だが，タイプヒントすると<class 'str'>が最初に入るのでやらない
        self.__buffer = []

    def make_title(self, title: str):
        self.__buffer.append("====================\n")
        self.__buffer.append("『{}』\n".format(title))
        self.__buffer.append("\n")

    def make_string(self, string: str):
        self.__buffer.append("■{}\n".format(string))
        self.__buffer.append("\n")

    def make_items(self, items: [str]):
        for item in items:
            self.__buffer.append("    ・{}\n".format(item))
        self.__buffer.append("\n")

    def close(self):
        self.__buffer.append("====================\n")

    def get_result(self) -> str:
        return "".join(self.__buffer)
