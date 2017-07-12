#!/usr/bin/env python
# coding: utf-8

from singleton import Singleton

print("Start.")
obj1 = Singleton()
obj2 = Singleton()

if (id(obj1) == id(obj2)):
    print("obj1とobj2は同じインスタンスです")
else:
    print("obj1とobj2は同じインスタンスではありません")