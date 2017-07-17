#!/usr/bin/env python
# coding: utf-8

from .product import Product


class Manager(object):
    def __init__(self):
        self.__showcase = {}

    def register(self, name: str, proto: Product) -> None:
        self.__showcase[name] = proto

    def create(self,protoname:str) ->Product:
        p = self.__showcase.get(protoname,"NoProduct")
        return p.create_clone()