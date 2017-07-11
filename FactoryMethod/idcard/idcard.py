#!/usr/bin/env python
# coding: utf-8

import sys, os

sys.path.append(os.pardir)
from framework.product import Product

class IDCard(Product):
    def __init__(self, owner: str):
        self.owner = owner
        print("{}のカードを作ります．".format(self.owner))

    def use(self):
        print("{}のカードを使います．".format(self.owner))

    def get_owner(self) -> str:
        return self.owner
