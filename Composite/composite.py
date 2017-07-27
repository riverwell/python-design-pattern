#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod

import better_exceptions


# ファイルに対してaddを呼び出した時に投げられる例外
class FileTreatmentException(Exception):
    def __init__(self):
        print("FileTreatmentException raised")


class Entry(metaclass=ABCMeta):
    # def __init__(self):
    #    raise Exception("Abstract class")

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_size(self) -> int:
        raise NotImplementedError

    def add(self, entry: 'Entry'):
        raise FileTreatmentException

    def print_list(self):
        self._print_list("")

    @abstractmethod
    def _print_list(self, prefix: str):
        # prefixを前につけて一覧を表示する
        raise NotImplementedError

    def __str__(self):
        return "{name} ({size})".format(name=self.get_name(), size=self.get_size())


class File(Entry):
    def __init__(self, name: str, size: int):
        self.__name = name
        self.__size = size

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def _print_list(self, prefix: str):
        print("{prefix}/{this}".format(prefix=prefix, this=str(self)))


class Directory(Entry):
    def __init__(self, name):
        self.__name = name
        self.__directory = []

    def get_name(self):
        return self.__name

    def get_size(self) -> int:
        size = 0
        for entry in self.__directory:
            size += entry.get_size()
        return size

    def add(self, entry: 'Entry'):
        self.__directory.append(entry)

    def _print_list(self, prefix: str):
        print("{prefix}/{this}".format(prefix=prefix, this=str(self)))
        for entry in self.__directory:
            entry._print_list("{prefix}/{this}".format(prefix=prefix, this=self.__name))


def main():
    try:
        print("Making root entries...")
        rootdir = Directory("root")
        bindir = Directory("bin")
        tmpdir = Directory("tmp")
        userdir = Directory("usr")
        rootdir.add(bindir)
        rootdir.add(tmpdir)
        rootdir.add(userdir)

        # bindirとrootdirの中身が同じになってる，，，なぜだ
        bindir.add(File("vi", 10000))
        bindir.add(File("latex", 20000))
        rootdir.print_list()

        print("")
        print("Making user entries...")
        yuki = Directory("yuki")
        hanako = Directory("hanako")
        tomura = Directory("tomura")
        userdir.add(yuki)
        userdir.add(hanako)
        userdir.add(tomura)

        yuki.add(File("diary.html", 100))
        yuki.add(File("Composite.java", 200))
        hanako.add(File("memo.tex", 300))
        tomura.add(File("game.doc", 400))
        tomura.add(File("junk.mail", 500))
        rootdir.print_list()
    except FileTreatmentException as e:
        print(e)


if __name__ == "__main__":
    main()
