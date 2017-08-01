#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod
from zope.interface import Interface, implementer


class Display(metaclass=ABCMeta):
    @abstractmethod
    def get_columns(self) -> int:
        """
        # 横の文字数を得る
        :return:
        """

    @abstractmethod
    def get_rows(self) -> int:
        """
        縦の行数を得る
        :return:
        """

    @abstractmethod
    def get_row_text(self, row: int) -> str:
        """
        row番目の文字列を得る
        :param row:
        :return:
        """

    def show(self):
        """
        全部表示する
        :return:
        """
        for i in range(self.get_rows()):
            print(self.get_row_text(i))


class StringDisplay(Display):
    def __init__(self, string: str):
        self.__string = string  # 表示文字列

    def get_columns(self):
        return len(self.__string.encode("utf-8"))  # 文字数

    def get_rows(self):
        return 1  # 行数は1

    def get_row_text(self, row: int):
        if row == 0:  # rowが0のときのみ返す
            return self.__string
        else:
            return None


class Border(Display, metaclass=ABCMeta):
    def __init__(self, display: Display):  # インスタンス生成時に中身を引数で指定
        self._display = display  # この飾り枠がくるんでいる中身を指す


class SideBorder(Border):
    def __init__(self, display: Display, ch: str):
        super().__init__(display)
        self.__border_char = ch

    def get_columns(self):
        return 1 + self._display.get_columns() + 1  # 文字数は中身の両側に文字分を加えたもの

    def get_rows(self):
        return self._display.get_rows()  # 行数は中身の行数と同じ

    def get_row_text(self, row: int):  # 指定行の内容は，中身の指定行の両側に飾り文字を付けたもの
        return self.__border_char + self._display.get_row_text(row) + self.__border_char


class FullBorder(Border):
    def __init__(self, display: Display):
        super().__init__(display)

    def get_columns(self):
        return 1 + self._display.get_columns() + 1  # 文字数は中身の両側に文字分を加えたもの

    def get_rows(self):
        return 1 + self._display.get_rows() + 1  # 行数は中身の行数に上下の文字分を加えたもの

    def get_row_text(self, row: int):  # 指定行の内容
        if row == 0:  # 枠の上端
            return '+' + self.__make_line('-', self._display.get_columns()) + '+'
        elif row == self._display.get_rows() + 1:  # 枠の下端
            return '+' + self.__make_line('-', self._display.get_columns()) + '+'
        else:  # それ以外
            return '|' + self._display.get_row_text(row - 1) + '|'

    def __make_line(self, ch: str, count: int):
        buf = []
        for i in range(count):
            buf.append(ch)
        return "".join(buf)


def main():
    b1 = StringDisplay("Hello, world.")
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)
    b1.show()
    b2.show()
    b3.show()
    b4 = SideBorder(FullBorder(FullBorder(SideBorder(FullBorder(StringDisplay("こんにちは．")), '*'))), '/')
    b4.show()


if __name__ == "__main__":
    main()
