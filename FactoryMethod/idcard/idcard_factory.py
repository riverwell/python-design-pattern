#!/usr/bin/env python
# coding: utf-8

import sys, os
from .idcard import IDCard

sys.path.append(os.pardir)
from framework.product import Product
from framework.factory import Factory


class IDCardFactory(Factory):
    def __init__(self):
        self.owners = [str]

    def create_product(self, owner: str):
        return IDCard(owner)

    def register_product(self, product: Product):
        self.owners.append(product.get_owner())

    def get_owners(self) -> []:
        return self.owners
