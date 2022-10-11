import string


class Tokenizer():

    def tokenize(self, line):
        for punct in string.punctuation:
            line = line.replace(punct, "")

        return ((line.strip()).lower()).split()