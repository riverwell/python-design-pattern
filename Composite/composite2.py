#!/usr/bin/env python
# -*- coding: utf8 -*-

class FileTreatmentException(Exception):
    def __init__(self):
        print("FileTreatmentException raised")


class Entry:
    def __init__(self):
        raise Exception("Abstract class")

    def getName(self):
        raise NotImplementedError

    def getSize(self):
        raise NotImplementedError

    def printList(self):
        self._printList("")

    def _printList(self, prefix):
        raise NotImplementedError

    def add(self, entry):
        raise FileTreatmentException

    def __str__(self): return "%s (%d)" % (self.getName(), self.getSize())

    # 11-2
    def getFullName(self):
        entry = self
        fullname = ""
        while entry is not None:
            fullname = "/" + entry.getName() + fullname
            entry = entry.parent
        return fullname


class File(Entry):
    def __init__(self, name, size):
        self.__name = name
        self.__size = size
        self.parent = None

    def getName(self): return self.__name

    def getSize(self): return self.__size

    def _printList(self, prefix):
        print(prefix + "/" + str(self))


class Directory(Entry):
    def __init__(self, name):
        self.__name = name
        self.directory = []
        self.parent = None

    def getName(self):
        return self.__name

    def getSize(self):
        return sum([e.getSize() for e in self.directory])

    def _printList(self, prefix):
        print(prefix + "/" + str(self))

        for e in self.directory:
            e._printList(prefix + "/" + self.__name)

    def add(self, entry):
        self.directory.append(entry)
        entry.parent = self  # 11-2


def main():
    print("Making root entries...")
    m_rootdir = Directory("root")
    m_bindir = Directory("bin")
    m_tmpdir = Directory("tmp")
    m_usrdir = Directory("usr")
    m_rootdir.add(m_bindir)
    m_rootdir.add(m_tmpdir)
    m_rootdir.add(m_usrdir)
    m_bindir.add(File("vi", 10000))
    m_bindir.add(File("latex", 20000))
    m_rootdir.printList()

    print("")

    print("Making user entries...")

    m_yuki = Directory("yuki")
    m_hanako = Directory("hanako")
    m_tomura = Directory("tomura")
    m_usrdir.add(m_yuki)
    m_usrdir.add(m_hanako)
    m_usrdir.add(m_tomura)
    m_yuki.add(File("diary.html", 100))
    m_yuki.add(File("Composite.java", 200))
    m_hanako.add(File("memo.tex", 300))
    m_tomura.add(File("game.doc", 400))
    m_tomura.add(File("junk.mail", 500))
    m_rootdir.printList()

    # 11-2
    print("")

    print("#11-2")

    m_rootdir = Directory("root")
    m_usrdir = Directory("usr")
    m_rootdir.add(m_usrdir)
    m_yuki = Directory("yuki")
    m_usrdir.add(m_yuki)
    m_file = File("Composite.java", 100)
    m_yuki.add(m_file)
    m_rootdir.printList()
    print("file = " + m_file.getFullName())
    print("yuki = " + m_yuki.getFullName())


if __name__ == '__main__':
    main()
