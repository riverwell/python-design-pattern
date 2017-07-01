#!/usr/bin/env python
# coding: utf-8

from iterator import Iterator


class BookShelfIterator(Iterator):
    def __init__(self, book_shelf):
        self.book_shelf = book_shelf
        self.index = 0

    def has_next(self):
        if (self.index < self.book_shelf.get_length()):
            return True
        else:
            return False

    def next(self):
        book = self.book_shelf.get_book_at(self.index)
        self.index += 1
        return book
