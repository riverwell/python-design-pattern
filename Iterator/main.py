#!/usr/bin/env python
# coding: utf-8

from book_shelf import BookShelf
from book import Book

book_shelf = BookShelf()
book_shelf.append_book(Book("Around the World in 80 Days"))
book_shelf.append_book(Book("Bible"))
book_shelf.append_book(Book("Cinderella"))
book_shelf.append_book(Book("Daddy-Long-Legs"))
it = book_shelf.iterator()
while (it.has_next()):
    book = it.next()
    print(book.get_name())
