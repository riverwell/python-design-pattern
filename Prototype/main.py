#!/usr/bin/env python
# coding: utf-8

from framework.manager import Manager
from message_box import MessageBox
from underline_pen import UnderlinePen

manager = Manager()

upen = UnderlinePen('~')
mbox = MessageBox('*')
sbox = MessageBox('/')

manager.register("strong message", upen)
manager.register("warning box", mbox)
manager.register("slash box", sbox)

p1 = manager.create("strong message")
p1.use("こんにちは")
p2 = manager.create("warning box")
p2.use("Hello, world")
p3 = manager.create("slash box")
p3.use("Hello, world.")
