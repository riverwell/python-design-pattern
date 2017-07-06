#!/usr/bin/env python
# coding: utf-8

from print_banner import PrintBanner, TransferPrintBanner
from print import Print

p = PrintBanner("Hello")
p.print_weak()
p.print_strong()

tp = TransferPrintBanner("Good bye")
tp.print_weak()
tp.print_strong()
