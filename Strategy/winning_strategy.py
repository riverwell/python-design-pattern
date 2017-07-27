#!/usr/bin/env python
# coding: utf-8

import random

from zope.interface import implementer

from strategy import Strategy
from hand import Hand


@implementer(Strategy)
class WinningStrategy:
    __won = False
    __prev_hand = None

    def __init__(self, seed: int):
        random.seed(seed)

    def next_hand(self) -> int:
        if not (self.__won):
            self.__prev_hand = Hand(3).get_hand(random.randint(0, 2))
        return self.__prev_hand

    def study(self, win: bool):
        self.__won = win
