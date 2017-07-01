#!/usr/bin/env python
# coding: utf-8

from abc import abstractmethod


# 数え上げる集合体を表す
class Aggregate(object):
    # Iteratorを1個作成する
    @abstractmethod
    def iterator(self):
        pass
