#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod


# Iteratorインターフェース
class Iterator(object):
    # 次の要素が存在するか調べる(次にnextメソッドを呼んでも大丈夫か調べる)
    @abstractmethod
    def has_next(self):
        pass

    # 次の要素を得る
    @abstractmethod
    def next(self):
        pass
