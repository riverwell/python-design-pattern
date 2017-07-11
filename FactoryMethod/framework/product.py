#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass
