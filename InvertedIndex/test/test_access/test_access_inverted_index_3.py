import random
from unittest import TestCase
import os
from time import time
from Lib.Program.Controller import Controller
from Lib.indexs.Index_3.InvertedIndex import InvertedIndex


class test_access_index_1(TestCase):

    index = InvertedIndex()

    books = os.listdir("../../books/xml")
    for i in range(len(books)):
        books[i] = "../../books/xml/" + books[i]

    Controller().inverted_index_of(index, books, False)

    words = list(index.get_inverted_index().keys())
    start = time()
    for i in range(100000):
        books = []
        word = random.choice(words)
        list_tuples = index.get_inverted_index()[word]
        for tuple in list_tuples:
            if tuple[0] not in books:
                books.append(tuple[0])
    end = time()
    print("The time needed accces n times to inverted index was ", end - start)

    pass