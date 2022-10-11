import os


class InvertedIndexStore:

    def __init__(self, inverted_index):
        self._inverted_index = inverted_index

    def store(self):
        serialized_inverted_index, store_name = self._inverted_index.serialize()

        with open("../../json_inverted_index/" + store_name, 'w') as f:
            f.write(serialized_inverted_index)




