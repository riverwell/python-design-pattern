#!/usr/bin/env python
# coding: utf-8

from zope.interface import implementer
from framework.product import Product
import copy


@implementer(Product)
class MessageBox():
    def __init__(self, decochar):
        self.__decochar = decochar

    def use(self, s: str):
        # 文字列の長さを取る（utf-8は日本語1文字3バイトなので，長さ合わないが）
        length = len(s.encode("utf-8"))
        for i in range(length + 4):
            print(self.__decochar, end='')
        print()
        print("{d} {s} {d}".format(d=self.__decochar, s=s))
        for i in range(length + 4):
            print(self.__decochar, end='')
        print()

    # 本の通りにやると，インターフェイスであって継承してるわけじゃないから，Productをかえしてないことになる
    def create_clone(self) -> 'Product':
        p = None
        try:
            # 浅いコピーを行なう
            p = copy.copy(self)
        except:
            pass
        return p
