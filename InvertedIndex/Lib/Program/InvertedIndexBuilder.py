import os

from stop_words import get_stop_words

from Lib.Program.Tokenizer import Tokenizer


class InvertedIndexBuilder:

    def __init__(self, inverted_index):
        self.inverted_index = inverted_index

    def build(self, document):

        tokenizer = Tokenizer()
        n_line = 0
        with open(document.get_name_document()) as text:
            for line in text:
                n_line += 1
                list_words = tokenizer.tokenize(line)

                for word in list_words:
                    if word in get_stop_words('english') or len(word) == 0:
                        pass
                    else:
                        self.inverted_index.add_word(word, document.get_metadata().get_id(), n_line)

