#!/usr/bin/env python
# coding: utf-8

class Book(object):
    def __init__(self, name):
        self.name = name

    # 本の名前を得る
    def get_name(self):
        return self.name
