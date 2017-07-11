#!/usr/bin/env python
# coding: utf-8

from framework.factory import Factory
from framework.product import Product

from idcard.idcard import IDCard
from idcard.idcard_factory import IDCardFactory

factory = IDCardFactory()
card1 = factory.create("結城浩")
card2 = factory.create("とむら")
card3 = factory.create("佐藤花子")
card1.use()
card2.use()
card3.use()
