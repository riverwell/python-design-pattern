#!/usr/bin/env python
# coding: utf-8


import random
import time

import better_exceptions


class Memento:
    def __init__(self, money: int):
        self._money = money
        self.fruits = []

    def get_money(self) -> int:
        """
        所持金を得る
        :return:
        """
        return self._money

    def add_fruit(self, fruit: str):
        """
        フルーツを追加する
        :param fruit:
        :return:
        """
        self.fruits.append(fruit)

    def get_fruits(self):
        return self.fruits


class Gamer:
    def __init__(self, money: int):
        self.__money: int = money
        self.__fruits = []
        self.__random = random
        self.__random.seed(0)
        self.__fruits_name = ['リンゴ', 'ぶどう', 'バナナ', 'みかん', ]

    def get_money(self):
        """
        現在の所持金を得る
        :return:
        """
        return self.__money

    def bet(self):
        dice: int = self.__random.randint(0, 5) + 1
        print(dice)
        if dice == 1:
            self.__money += 100
            print('所持金が増えました．')
        elif dice == 2:
            self.__money /= 2
            print("所持金が半分になりました．")
        elif dice == 6:
            f = self.__get_fruit()
            print('フルーツ(' + f + ')をもらいました．')
            self.__fruits.append(f)
        else:
            print('何も起こりませんでした．')

    def create_memento(self) -> Memento:
        """
        スナップショットを撮る
        :return:
        """
        m = Memento(self.__money)
        for fruit in self.__fruits:
            # フルーツはおいしいものだけ保存
            if fruit.startswith('おいしい'):
                m.add_fruit(fruit)
        return m

    def restore_memento(self, memento: Memento):
        """
        アンドゥを行なう
        :param memento:
        :return:
        """
        self.__money = memento.get_money()
        self.__fruits = memento.get_fruits()

    def __repr__(self):
        """
        文字列表現
        :return:
        """
        return '[money = {}, fruits = {}]'.format(self.__money, self.__fruits)

    def __get_fruit(self):
        prefix = ''
        if self.__random.choice([True, False]):
            prefix = 'おいしい'
        return '{} {}'.format(prefix,self.__fruits_name[self.__random.randint(0, len(self.__fruits_name)-1)])
        # prefix + self.__fruits_name[self.__random.randint(0, len(self.__fruits_name))]


def main():
    # 引数を解析
    gamer: Gamer = Gamer(100)
    memento: Memento = gamer.create_memento()
    for i in range(100):
        print('==== ', i)
        print('現状：', gamer)
        gamer.bet()
        print('所持金は', gamer.get_money(), '円になりました．')

        # Mementoの取扱の決定
        if gamer.get_money() > memento.get_money():
            print('     (だいぶ増えたので，現在の状態を保存しておこう) ')
            memento = gamer.create_memento()
        elif gamer.get_money() < memento.get_money() / 2:
            print('     (だいぶ減ったので，以前の状態に復帰しよう) ')
            gamer.restore_memento(memento)

        # 時間待ち
        try:
            time.sleep(0.1)
        except InterruptedError as e:
            pass
        print('')


if __name__ == "__main__":
    main()
