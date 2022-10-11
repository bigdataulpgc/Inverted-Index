class Document:

    def __init__(self):
        self._metadata = None
        self._name_document = None

    def get_metadata(self):
        return self._metadata

    def set_metadata(self, new_metadata):
        if new_metadata != "None":
            self._metadata = new_metadata
        return self

    def get_name_document(self):
        return self._name_document

    def set_name_document(self, new_name_document):
        if new_name_document != "None":
            self._name_document = new_name_document
        return self
