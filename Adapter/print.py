#!/usr/bin/env python
# coding: utf-8


from zope.interface import Interface
from abc import ABCMeta, abstractmethod


# Printインターフェイス
class Print(Interface):
    def print_weak(self):
        pass

    def print_strong(self):
        pass


# 委譲を使う実装
class TransferPrint(metaclass=ABCMeta):
    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass
