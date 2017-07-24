#!/usr/bin/env python
# coding: utf-8

from display import Display


class CountDisplay(Display):
    # def __init__(self, impl: 'DisplayImpl'):
    #    super().__init__(impl)
    def multi_display(self, times: int):
        """
        times回繰り返して表示する
        :param times:
        :return:
        """
        self.open()
        for i in range(times):
            self.print()
        self.close()
