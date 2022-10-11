from Lib.Program.DocumentReader import DocumentReader
from Lib.Program.InvertedIndexBuilder import InvertedIndexBuilder
from Lib.Program.InvertedIndexStore import InvertedIndexStore


class Controller:

    def inverted_index_of(self, inverted_index, document_list, store):

        inverted_index_builder = InvertedIndexBuilder(inverted_index)

        for name_document in document_list:
            document_reader = DocumentReader(name_document)
            document = document_reader.read_document()
            inverted_index_builder.build(document)


        if store:
            InvertedIndexStore(inverted_index).store()

