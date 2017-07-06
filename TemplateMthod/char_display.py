#!/usr/bin/env python
# coding: utf-8

from abstract_display import AbstractDisplay


class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print("<<",end="")

    def print(self):
        print(self.ch,end="")

    def close(self):
        print(">>")
