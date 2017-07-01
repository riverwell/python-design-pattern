#!/usr/bin/env python
# coding: utf-8

from aggregate import Aggregate
from book import Book
from book_shelf_iterator import BookShelfIterator


class BookShelf(Aggregate):
    def __init__(self):
        self.books = []

    #
    def get_book_at(self, index):
        return self.books[index]

    def append_book(self, book):
        self.books.append(book)

    def get_length(self):
        return len(self.books)

    # BookShelfのイテレータを返す(本棚の本を数えたいとき呼び出す)
    def iterator(self):
        return BookShelfIterator(self)
