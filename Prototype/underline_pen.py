#!/usr/bin/env python
# coding: utf-8


from zope.interface import implementer
from framework.product import Product
import copy


@implementer(Product)
class UnderlinePen():
    def __init__(self, ulchar):
        self.__ulchar = ulchar

    def use(self, s: str):
        # 文字列の長さを取る（utf-8は日本語1文字3バイトなので，長さ合わないが）
        length = len(s.encode("utf-8"))

        print("\" {s} \"".format(d=self.__ulchar, s=s))
        for i in range(length + 4):
            print(self.__ulchar, end='')
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
