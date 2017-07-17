#!/usr/bin/env python
# coding: utf-8

from builder import Builder


class HtmlBuilder(Builder):
    def __init__(self):
        # str型だが，タイプヒントすると<class 'str'>が最初に入るのでやらない
        self.__buffer = []
        self.__filename = None

    def make_title(self, title: str):
        self.__filename = "{}.html".format(title)
        self.__buffer.append("<html><head><title>{}</title></head><body>\n".format(title))
        # タイトルを出力
        self.__buffer.append("<h1>{}</h1>\n".format(title))

    def make_string(self, string: str):
        self.__buffer.append("<p>{}</p>\n".format(string))

    def make_items(self, items: [str]):
        self.__buffer.append("<ul>")
        for item in items:
            self.__buffer.append("<li>{}</li>\n".format(item))
        self.__buffer.append("</ul>\n")

    def close(self):
        self.__buffer.append("</body></html>\n")
        with open(self.__filename, "w") as f:
            f.write("".join(self.__buffer))

    def get_result(self) -> str:
        return self.__filename
