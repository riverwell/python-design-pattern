#!/usr/bin/env python
# coding: utf-8

# http://blanktar.jp/blog/2016/07/python-singleton.html

import threading


class Singleton(object):
    __instance = None
    # スレッドセーフにする
    __lock = threading.Lock()

    # newは必ず呼ばれる(initは呼ばれないこともある)
    # pythonではコンストラクタをprivateにできないので，__new__を使う
    # __new__は__init__の前に呼ばれる
    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
                print("インスタンスを生成しました")
        return cls.__instance

    def __init__(self):
        print("init")

        # pythonではstaticメソッド，classメソッドともにインスタンス変数にアクセスできない
        # クラスメソッドでは，第一引数にクラスを渡すので，渡ってきたクラスを使って，クラス変数にアクセスできる
        # @classmethod
        # def get_instance(cls):
        #    return cls.__instance
