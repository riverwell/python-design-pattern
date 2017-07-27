#!/usr/bin/env python
# coding: utf-8

from strategy import Strategy


class Player:
    __wincount = 0
    __losecount = 0
    __gamecount = 0

    def __init__(self, name: str, strategy: Strategy):
        self.name = name
        self.strategy = strategy

    def next_hand(self):
        return self.strategy.next_hand()

    def win(self):
        self.strategy.study(True)
        self.__wincount += 1
        self.__gamecount += 1

    def lose(self):
        self.strategy.study(False)
        self.__losecount += 1
        self.__gamecount += 1

    def even(self):
        self.__gamecount += 1

    def to_string(self) -> str:
        return "[{name}:{gamecount} games, {wincount} win, {losecount} lose]".format(name=self.name,
                                                                                     gamecount=self.__gamecount,
                                                                                     wincount=self.__wincount,
                                                                                     losecount=self.__losecount)
