import json as js

class Reference:

    def __init__(self):
        self._document_id = None
        self._lines = []

    def get_document_id(self):
        return self._document_id

    def set_document_id(self, document_id):
        self._document_id = document_id
        return self

    def get_lines(self):
        return self._lines

    def add_line(self, line):
        self._lines.append(line)
        return self

    def serialize(self):
        return js.dumps(self.__dict__)
