from Lib.indexs.AbstractInvertedIndex import AbstractInvertedIndex
from Lib.indexs.Index_2.Reference import Reference


class InvertedIndex(AbstractInvertedIndex):

    def __init__(self):
        self._inverted_index = {}

    def get_inverted_index(self):
        return self._inverted_index

    def set_inverted_index(self, new_inverted_index):
        self._inverted_index = new_inverted_index

    def add_word(self, word, document_id, n_line):

        if word in self._inverted_index:
            for reference in self._inverted_index[word]:
                if reference.get_document_id() == document_id:
                    reference.add_line(n_line)
                    break
            (self._inverted_index[word]).append(Reference().set_document_id(document_id).add_line(n_line))
        else:
            self._inverted_index[word] = [Reference().set_document_id(document_id).add_line(n_line)]

