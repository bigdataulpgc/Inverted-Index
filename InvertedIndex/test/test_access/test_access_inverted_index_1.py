from unittest import TestCase
import os
import random
from time import time
from Lib.Program.Controller import Controller
from Lib.indexs.Index_1.InvertedIndex import InvertedIndex


class test_access_index_1(TestCase):

    index = InvertedIndex()

    books = os.listdir("../../books/xml")
    for i in range(len(books)):
        books[i] = "../../books/xml/" + books[i]

    Controller().inverted_index_of(index, books, False)

    words = list(index.get_inverted_index().keys())
    start = time()
    for i in range(100000):
        word = random.choice(words)
        books = list(index.get_inverted_index()[word].keys())
    end = time()
    print("The time needed accces 100000 times to inverted index was ", end - start)

    pass