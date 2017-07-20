#!/usr/bin/env python
# coding: utf-8

import argparse

from factory.link import Link
from factory.tray import Tray
from factory.factory import Factory
from factory.page import Page


def main():
    # 引数を解析
    parser = argparse.ArgumentParser()
    parser.add_argument("--f")
    args = parser.parse_args()

    # 引数を変数に設定
    factory_name = args.f

    # print(factory_name)
    factory = Factory.get_factory(factory_name)

    # print(type(factory))

    asahi = factory.create_link(caption="朝日新聞", url="http://www.asahi.com/")
    yomiuri = factory.create_link("読売新聞", "http://www.yomiuri.co.jp/")

    us_yahoo = factory.create_link("Yahoo!", "http://www.yahoo.com/")
    jp_yahoo = factory.create_link("Yahoo!Japan", "http://www.yahoo.co.jp/")

    excite = factory.create_link("Excite", "http://www.excite.com/")
    google = factory.create_link("Google", "http://www.google.com/")

    traynews = factory.create_tray("新聞")
    traynews.add(asahi)
    traynews.add(yomiuri)

    trayyahoo = factory.create_tray("Yahoo!")
    trayyahoo.add(us_yahoo)
    trayyahoo.add(jp_yahoo)

    traysearch = factory.create_tray("サーチエンジン")
    traysearch.add(trayyahoo)
    traysearch.add(excite)
    traysearch.add(google)

    page = factory.create_page("LinkPage", "結城 浩")
    page.add(traynews)
    page.add(traysearch)
    page.output()


if __name__ == "__main__":
    main()
