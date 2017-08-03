#!/usr/bin/env python
# coding: utf-8

from abc import ABCMeta, abstractmethod

from zope.interface import Interface, implementer
from functools import singledispatch, update_wrapper
import better_exceptions


def method_dispatch(func):
    dispatcher = singledispatch(func)

    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)

    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper


# ファイルに対してaddを呼び出した時に投げられる例外
class FileTreatmentException(Exception):
    def __init__(self):
        print("FileTreatmentException raised")


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    @singledispatch
    def visit(self, entry):
        pass

    @abstractmethod
    @visit.register('File')
    def _(self, file):
        pass

    @abstractmethod
    @visit.register('Directory')
    def _(self, directory):
        pass


class Element(Interface):
    @abstractmethod
    def accept(self, v: Visitor):
        pass


@implementer(Element)
class Entry(metaclass=ABCMeta):
    def get_name(self) -> str:
        """
        名前を得る
        :return:
        """

    def get_size(self) -> int:
        """
        サイズを得る
        :return:
        """

    def add(self, entry: 'Entry') -> 'Entry':
        raise FileTreatmentException

    def iterator(self):
        raise FileTreatmentException

    def __str__(self):
        return "{name} ({size})".format(name=self.get_name(), size=self.get_size())


class File(Entry):
    def __init__(self, name: str, size: int):
        self.__name = name
        self.__size = size

    def get_name(self) -> str:
        return self.__name

    def get_size(self) -> int:
        return self.__size

    def accept(self, v: 'Visitor'):
        v.visit(self)


class Directory(Entry):
    def __init__(self, name: str):
        self.__dir = []
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_size(self) -> int:
        size = 0
        for ele in self.__dir:
            size += ele.get_size()
        return size

    def add(self, entry: 'Entry'):
        self.__dir.append(entry)

    def iterator(self):
        return self.__dir

    def accept(self, v: 'Visitor'):
        v.visit(self)


class ListVisitor(Visitor):
    def __init__(self):
        self.__current_dir = ""

    @method_dispatch
    def visit(self, entry):
        print("visit call")

    @visit.register(File)
    def _(self, file):
        print(self.__current_dir + '/' + str(file))

    @visit.register(Directory)
    def _(self, directory):
        print(self.__current_dir + "/" + str(directory))
        savedir = self.__current_dir
        self.__current_dir = self.__current_dir + '/' + directory.get_name()
        for ele in directory.iterator():
            ele.accept(self)
        self.__current_dir = savedir


def main():
    try:
        print("Making root entries...")
        rootdir = Directory("root")
        bindir = Directory("bin")
        tmpdir = Directory("tmp")
        usrdir = Directory("usr")
        rootdir.add(bindir)
        rootdir.add(tmpdir)
        rootdir.add(usrdir)
        bindir.add(File("vi", 10000))
        bindir.add(File("latex", 20000))
        rootdir.accept(ListVisitor())

        print("")
        print("Making user entries...")
        yuki = Directory("yuki")
        hanako = Directory("hanako")
        tomura = Directory("tomura")
        usrdir.add(yuki)
        usrdir.add(hanako)
        usrdir.add(tomura)
        yuki.add(File("diary.html", 100))
        yuki.add(File("Composite.java", 200))
        hanako.add(File("memo.tex", 300))
        tomura.add(File("game.doc", 400))
        tomura.add(File("junk.mail", 500))
        rootdir.accept(ListVisitor())
    except(FileTreatmentException):
        raise FileTreatmentException


if __name__ == "__main__":
    main()
