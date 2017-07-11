#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod

from framework.product import Product


class Factory(metaclass=ABCMeta):
    def create(self, owner: str) -> Product:
        p = self.create_product(owner)
        self.register_product(p)
        return p

    # 例題ではprotectedだったが，pythonにprotectedはないし，privateにするとエラー吐くのでpublicにした
    @abstractmethod
    def create_product(self, owner: str) -> Product:
        pass

    @abstractmethod
    def register_product(self, product: Product):
        pass
