#!/usr/bin/env python
# coding: utf-8


class Hand:
    __HANDVALUE_GUU = 0  # グー
    __HANDVALUE_CHO = 1  # チー
    __HANDVALUE_PAA = 2  # パー
    __hand = [__HANDVALUE_GUU, __HANDVALUE_CHO, __HANDVALUE_PAA]
    __name = ["グー", "チョキ", "パー"]

    def __init__(self, handvalue: int):
        self.handvalue = handvalue

    def get_hand(self, handvalue: int) -> int:
        return self.__hand[handvalue]

    def is_stronger_than(self, h: 'Hand') -> bool:
        return self.__fight(h) == 1

    def is_weaker_than(self, h: 'Hand') -> bool:
        return self.__fight(h) == -1

    def __fight(self, h: 'Hand') -> int:
        # あいこ
        if self.handvalue == h.handvalue:
            return 0
        # selfの勝ち
        elif (self.handvalue + 1) % 3 == h.handvalue:
            return 1
        # selfの負け
        else:
            return -1

    def to_string(self) -> str:
        return self.__name[self.handvalue]
