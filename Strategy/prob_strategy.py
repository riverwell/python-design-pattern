#!/usr/bin/env python
# coding: utf-8

import random

from zope.interface import implementer

from strategy import Strategy
from hand import Hand


@implementer(Strategy)
class ProbStrategy:
    __prev_hand_value = 0
    __current_hand_value = 0
    __history = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    def __init__(self, seed: int):
        random.seed(seed)

    def next_hand(self):
        bet = random.randint(0, self.get_sum(self.__current_hand_value))
        handvalue = 0
        if (bet < self.__history[self.__current_hand_value][0]):
            handvalue = 0
        elif (bet < self.__history[self.__current_hand_value][0] + self.__history[self.__current_hand_value][1]):
            handvalue = 1
        else:
            handvalue = 2
        self.__prev_hand_value = self.__current_hand_value
        self.__current_hand_value = handvalue
        return Hand(3).get_hand(handvalue)

    def get_sum(self, hv: int):
        __sum = 0
        for i in range(0, 2):
            __sum += self.__history[hv][i]
        return __sum

    def study(self, win: bool):
        if win:
            self.__history[self.__prev_hand_value][self.__current_hand_value] += 1
        else:
            self.__history[self.__prev_hand_value][(self.__current_hand_value + 1) % 3] += 1
            self.__history[self.__prev_hand_value][(self.__current_hand_value + 2) % 3] += 1
