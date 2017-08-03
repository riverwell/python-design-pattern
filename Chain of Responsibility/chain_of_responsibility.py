#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod
from functools import singledispatch
import argparse

from zope.interface import Interface, implementer
import better_exceptions


class Trouble():
    def __init__(self, number: int):
        self.__number = number

    def get_number(self) -> int:
        return self.__number

    def __str__(self):
        return "[Trouble {}]".format(self.__number)


class Support(metaclass=ABCMeta):
    # トラブル解決者の生成
    def __init__(self, name: str):
        self.__name = name
        self.__next = None

    # たらい回しの先を設定
    def set_next(self, nxt: 'Support'):
        self.__next = nxt
        return nxt

    # トラブル解決の手順
    def support(self, trouble: 'Trouble'):
        if (self._resolve(trouble)):
            self._done(trouble)
        elif (self.__next != None):
            self.__next.support(trouble)
        else:
            self._fail(trouble)

    @abstractmethod
    def _resolve(self, trouble: 'Trouble') -> bool:
        """
        解決用メソッド
        :param trouble:
        :return:
        """

    def _done(self, trouble: 'Trouble') -> None:
        """
        解決
        :param trouble:
        :return:
        """
        print("{trouble} is resolved by {this}".format(trouble=str(trouble), this=str(self)))

    def _fail(self, trouble: 'Trouble') -> None:
        """
        解決
        :param trouble:
        :return:
        """
        print("{trouble} cannot be resolved.".format(trouble=str(trouble)))

    def __str__(self):
        return "[{}]".format(self.__name)


# 自分は何も問題を処理しない
class NoSupport(Support):
    def __init__(self, name: str):
        super().__init__(name)

    def _resolve(self, trouble: 'Trouble'):
        return False


# limitで指定した番号未満のトラブルを解決するクラス
class LimitSupport(Support):
    def __init__(self, name: str, limit: int):
        super().__init__(name)
        self.__limit = limit

    def _resolve(self, trouble: 'Trouble'):
        if trouble.get_number() < self.__limit:
            return True
        else:
            return False


# 奇数番号のトラブルを解決
class OddSupport(Support):
    def __init__(self, name: str):
        super().__init__(name)

    def _resolve(self, trouble: 'Trouble'):
        if trouble.get_number() % 2 == 1:
            return True
        else:
            return False


# 指定した番号のトラブルを解決
class SpecialSupport(Support):
    def __init__(self, name: str, number: int):
        super().__init__(name)
        self.__number = number

    def _resolve(self, trouble: 'Trouble'):
        if trouble.get_number() == self.__number:
            return True
        else:
            return False


def main():
    # 引数を解析
    alice = NoSupport("Alice")
    bob = LimitSupport("Bob", 100)
    charlie = SpecialSupport("Charlie", 429)
    diana = LimitSupport("Diana", 200)
    elmo = OddSupport("Elmo")
    fred = LimitSupport("Fred", 300)

    alice.set_next(bob).set_next(charlie).set_next(diana).set_next(elmo).set_next(fred)
    # 様々なトラブルが発生
    for i in range(0, 500, 33):
        alice.support(Trouble(i))


if __name__ == "__main__":
    main()
