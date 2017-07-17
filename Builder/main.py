#!/usr/bin/env python
# coding: utf-8

import argparse
from text_builder import TextBuilder
from html_builder import HtmlBuilder
from director import Director


def main():
    # 引数を解析
    parser = argparse.ArgumentParser()
    parser.add_argument("--t")
    args = parser.parse_args()

    # 引数を変数に設定
    file_type = args.t

    if file_type == "plain":
        textbuilder = TextBuilder()
        director = Director(textbuilder)
        director.construct()
        result = textbuilder.get_result()
        print(result)
    elif file_type == "html":
        htmlbuilder = HtmlBuilder()
        director = Director(htmlbuilder)
        director.construct()
        filename = htmlbuilder.get_result()
        print("{}が作成されました".format(filename))
    else:
        usage()


def usage():
    print("Usage: python3 main.py plain            プレーンテキストで文章を作成")
    print("Usage: python3 main.py html            HTMLで文章を作成")


if __name__ == "__main__":
    main()
