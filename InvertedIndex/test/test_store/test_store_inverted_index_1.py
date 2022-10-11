from unittest import TestCase
import os
from time import time
from Lib.Program.Controller import Controller
from Lib.indexs.Index_1.InvertedIndex import InvertedIndex


class test_store_inverted_index_1(TestCase):

    index = InvertedIndex()


    books = os.listdir("../../books/xml")
    for i in range(len(books)):
        books[i] = "../../books/xml/" + books[i]

    start = time()
    Controller().inverted_index_of(index, books, True)
    end = time()
    print("The time needed to create the index number 1 was ", end - start)

    pass