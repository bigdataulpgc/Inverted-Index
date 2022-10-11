import xmltodict

from Lib.Program.DocumentBuilder import DocumentBuilder


class DocumentReader:

    def __init__(self, name_document):
        self.name_document = name_document
        self.document_builder = DocumentBuilder()

    def read_document(self):
        deserialized_document = self.deserializer(self.name_document)
        document = self.document_builder.build(deserialized_document)

        return document

    def deserializer(self, name_document):
        with open(name_document) as fd:
            deserialized_document = xmltodict.parse(fd.read())
            return deserialized_document
