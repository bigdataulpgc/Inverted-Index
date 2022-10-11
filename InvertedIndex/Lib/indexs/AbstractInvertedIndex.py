from abc import ABC, abstractmethod
import json as js


class AbstractInvertedIndex(ABC):

    def __init__(self):
        self.inverted_index = {}

    @abstractmethod
    def get_inverted_index(self):
        return self._inverted_index

    @abstractmethod
    def set_inverted_index(self, new_inverted_index):
        self._inverted_index = new_inverted_index

    @abstractmethod
    def add_word(self, word, document_id, n_line):
        pass