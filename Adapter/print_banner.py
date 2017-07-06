#!/usr/bin/env python
# coding: utf-8

from zope.interface import implementer

from banner import Banner
from print import Print, TransferPrint


@implementer(Print)
class PrintBanner(Banner):
    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()


class TransferPrintBanner(TransferPrint):
    def __init__(self, string):
        self.__banner = Banner(string)

    def print_weak(self):
        self.__banner.show_with_paren()

    def print_strong(self):
        self.__banner.show_with_aster()
