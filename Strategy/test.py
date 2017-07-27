#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random
from abc import ABCMeta, abstractmethod


class Hand():
    HANDVALUE_GUU = 0
    HANDVALUE_CHO = 1
    HANDVALUE_PAA = 2
    hand = [HANDVALUE_GUU, HANDVALUE_CHO, HANDVALUE_PAA]
    name = ["グー", "チョキ", "パー"]

    def __init__(self, handvalue):
        self.handvalue = handvalue

    def getHand(self, handvalue):
        return self.hand[handvalue]

    def isStrongerThan(self, h):
        return self.fight(h) == 1

    def isWeakerThan(self, h):
        return self.fight(h) == -1

    def fight(self, h):
        if self.handvalue == h.handvalue:
            return 0
        elif (self.handvalue + 1) % 3 == h.handvalue:
            return 1
        else:
            return -1

    def toString(self):
        return self.name[self.handvalue]


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def nextHand():
        pass

    @abstractmethod
    def study(win):
        pass


class WinningStrategy(Strategy):
    won = False
    prevHand = 0

    def __init__(self, _seed):
        random.seed(_seed)

    def nextHand(self):
        if not (self.won):
            self.prevHand = Hand(3).getHand(random.randint(0, 2))
        return self.prevHand

    def study(self, win):
        self.won = win


class ProbStrategy(Strategy):
    prevHandValue = 0
    currentHandValue = 0
    history = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    def __init__(self, _seed):
        random.seed(_seed)

    def nextHand(self):
        bet = random.randint(0, self.getSum(self.currentHandValue))
        handvalue = 0
        if bet < self.history[self.currentHandValue][0]:
            handvalue = 0
        elif bet < self.history[self.currentHandValue][0] + \
                self.history[self.currentHandValue][1]:
            handvalue = 1
        else:
            handvalue = 2
        self.prevHandValue = self.currentHandValue
        self.currentHandValue = handvalue
        return Hand(3).getHand(handvalue)

    def getSum(self, hv):
        _sum = 0
        for i in range(3):
            _sum += self.history[hv][i]
        return _sum

    def study(self, win):
        if win:
            self.history[self.prevHandValue][self.currentHandValue] += 1
        else:
            self.history[self.prevHandValue][(self.currentHandValue + 1) % 3] += 1
            self.history[self.prevHandValue][(self.currentHandValue + 2) % 3] += 1


class Player():
    wincount = 0
    losecount = 0
    gamecount = 0

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def nextHand(self):
        return self.strategy.nextHand()

    def win(self):
        self.strategy.study(True)
        self.wincount += 1
        self.gamecount += 1

    def lose(self):
        self.strategy.study(False)
        self.losecount += 1
        self.gamecount += 1

    def even(self):
        self.gamecount += 1

    def toStirng(self):
        return "[{0}: {1} games {2} win {3} lose]" \
            .format(self.name, self.gamecount, self.wincount, self.losecount)


def main():
    if len(sys.argv) != 3:
        sys.stdout.write("Usage: python Strategy.py randomseed1 randomseed2\n")
        sys.stdout.write("Example: python Strategy.py 314 15")
        sys.exit()
    seed1 = int(sys.argv[1])
    seed2 = int(sys.argv[2])
    player1 = Player("Taro", WinningStrategy(seed1))
    player2 = Player("Hana", ProbStrategy(seed2))
    for i in range(10000):  # 10000
        x = player1.nextHand()
        # x = 2
        nextHand1 = Hand(x)
        # print(x)
        y = player2.nextHand()
        nextHand2 = Hand(y)
        # print(y)
        if nextHand1.isStrongerThan(nextHand2):
            sys.stdout.write("Winner : {0}\n".format(player1.toStirng()))
            player1.win()
            player2.lose()
        elif nextHand2.isStrongerThan(nextHand1):
            sys.stdout.write("Winner : {0}\n".format(player2.toStirng()))
            player1.lose()
            player2.win()
        else:
            sys.stdout.write("Even ...\n")
            player1.even()
            player2.even()

    sys.stdout.write("Total result:\n")
    sys.stdout.write(player1.toStirng())
    sys.stdout.write("\n")
    sys.stdout.write(player2.toStirng())


if __name__ == "__main__":
    main()
