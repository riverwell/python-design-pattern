#!/usr/bin/env python
# coding: utf-8

import argparse
from abc import ABCMeta, abstractmethod
from functools import singledispatch
from configparser import ConfigParser
import logging

from zope.interface import Interface, implementer
import better_exceptions


class DataBase():
    @staticmethod
    def get_properties(dbname: str):
        filename = dbname + ".ini"
        conf = ConfigParser()
        try:
            conf.read(filename)
            return conf["MAIL"]
        except IOError:
            error_message = "Warning: {} is not found.".format(filename)
            print(error_message)
            logging.exception(error_message)


class HtmlWriter():
    def __init__(self, writer):
        self.__writer = writer

    def title(self, title: str):
        self.__writer.write("<html>")
        self.__writer.write("<head>")
        self.__writer.write("<title>{}</title>".format(title))
        self.__writer.write("</head>")
        self.__writer.write("<body>\n")
        self.__writer.write("<h1>{}</h1>\n".format(title))

    def paragraph(self, msg: str):
        self.__writer.write("<p>{}</p>\n".format(msg))

    def link(self, href: str, caption: str):
        self.paragraph("<a href=\"{href}\">{cap}</a>".format(href=href, cap=caption))

    def mailto(self, mailaddr: str, username: str):
        self.link("mailto:{mail}".format(mail=mailaddr), username)

    def close(self):
        self.__writer.write("</body>")
        self.__writer.write("</html>\n")
        self.__writer.close()


class PageMaker():
    @staticmethod
    def make_welcome_page(mailaddr: str, filename: str):
        try:
            mailprop = DataBase.get_properties("maildata")
            username = mailprop[mailaddr]
            with open(filename, "w") as f:
                writer = HtmlWriter(f)
                writer.title("Welcome to {}'s page!".format(username))
                writer.paragraph("{}のページへようこそ．".format(username))
                writer.paragraph("メール待っていますね．")
                writer.mailto(mailaddr, username)
                writer.close()
                print("{file} is created for {mail} ({user})".format(file=filename, mail=mailaddr, user=username))

        except IOError as e:
            logging.exception(e)


def main():
    PageMaker.make_welcome_page("hyuki@hyuki.com", "welcome.html")


if __name__ == "__main__":
    main()
