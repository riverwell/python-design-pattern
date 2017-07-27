#!/usr/bin/env python
# coding: utf-8

import argparse

import better_exceptions

from hand import Hand
from player import Player
from winning_strategy import WinningStrategy
from prob_strategy import ProbStrategy


def main():
    # 引数を解析
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed1")
    parser.add_argument("--seed2")
    args = parser.parse_args()

    # 引数を変数に設定
    seed1 = args.seed1
    seed2 = args.seed2
    player1 = Player("Taro", WinningStrategy(seed1))
    player2 = Player("Hana", ProbStrategy(seed2))
    for i in range(100):
        next_hand1 = Hand(player1.next_hand())
        next_hand2 = Hand(player2.next_hand())
        if (next_hand1.is_stronger_than(next_hand2)):
            print("Winner:{}".format(player1.to_string()))
            player1.win()
            player2.lose()
        elif (next_hand2.is_stronger_than(next_hand1)):
            print("Winner:{}".format(player2.to_string()))
            player1.lose()
            player2.win()
        else:
            print("Even...")
            player1.even()
            player2.even()
    print("Totla result:")
    print(player1.to_string())
    print(player2.to_string())


if __name__ == "__main__":
    main()
