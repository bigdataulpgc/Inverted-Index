from Lib.indexs.AbstractInvertedIndex import AbstractInvertedIndex
import json as js


class InvertedIndex(AbstractInvertedIndex):

    def __init__(self):
        self._inverted_index = {}

    def get_inverted_index(self):
        return self._inverted_index

    def set_inverted_index(self, new_inverted_index):
        self._inverted_index = new_inverted_index

    def serialize(self):
        return js.dumps(self._inverted_index, skipkeys=True, allow_nan=True, indent=6), "inverted_index3.json"

    def add_word(self, word, document_id, n_line):

        if word in self._inverted_index:
            self._inverted_index[word].append((document_id, n_line))
        else:
            self._inverted_index[word] = [(document_id, n_line)]