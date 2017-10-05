#!/usr/bin/env python
# coding: utf-8

import argparse
from abc import ABCMeta, abstractmethod
from functools import singledispatch
import random
import time

from zope.interface import Interface, implementer
import better_exceptions


class Observer(Interface):
    @abstractmethod
    def update(self, generator: 'NumberGenerator'):
        """"""


# NumberGeneratorクラス
class NumberGenerator(metaclass=ABCMeta):
    # observerを保持
    __observers = []

    # observerを追加
    def add_observer(self, observer: 'Observer'):
        self.__observers.append(observer)

    # observerを削除
    def delete_observers(self, observer: 'Observer'):
        self.__observers.remove(observer)

    # observerへ通知
    def notify_observers(self):
        for o in self.__observers:
            o.update(self)

    @abstractmethod
    def get_number(self) -> int:
        """"""

    @abstractmethod
    def execute(self):
        """"""


class RandomNumberGenerator(NumberGenerator):
    __number: int = 0

    def get_number(self):
        return self.__number

    def execute(self):
        for i in range(20):
            self.__number = random.randint(0, 50)
            self.notify_observers()


@implementer(Observer)
class DigitObserver:
    def update(self, generator: 'NumberGenerator'):
        print('DigitObserver:{}'.format(generator.get_number()))
        try:
            time.sleep(0.1)
        except InterruptedError:
            pass


@implementer(Observer)
class GraphObserver:
    def update(self, generator: 'NumberGenerator'):
        print('GraphObserver:')
        count = generator.get_number()
        for i in range(count):
            print('*', end='')
            try:
                time.sleep(0.1)
            except InterruptedError:
                pass
        print()


def main():
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()


if __name__ == "__main__":
    main()
