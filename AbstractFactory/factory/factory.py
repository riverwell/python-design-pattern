#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod
from factory.link import Link
from factory.tray import Tray


class Factory(metaclass=ABCMeta):
    @staticmethod
    def get_factory(classname: str):
        try:
            parts = classname.split('.')
            modules, kls = classname.rsplit(".", 1)
            m = __import__(modules)
            for comp in parts[1:]:
                m = getattr(m, comp)
                print(m)
            return m()
        except:
            print("クラスの作成に失敗しました．")
        return None

    @abstractmethod
    def create_link(self, caption: str, url: str) -> "Link":
        pass

    @abstractmethod
    def create_tray(self, caption: str) -> "Tray":
        pass

    @abstractmethod
    def create_page(self, title: str, author: str) -> "Page":
        pass