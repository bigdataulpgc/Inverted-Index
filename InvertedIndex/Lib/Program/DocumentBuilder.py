from Lib.Program.Document import Document
from Lib.Program.Metadata import Metadata


class DocumentBuilder:

    def build(self, deserialized_document):
        metadata = Metadata().set_id(deserialized_document['document']['id']).set_title(
            deserialized_document['document']['title']).set_release_date(
            deserialized_document['document']['release_date']). \
            set_posting_date(deserialized_document['document']['posting_date']).set_language(
            deserialized_document['document']['language'])

        for authors in (deserialized_document['document']['author']).split(","):
            metadata.add_authors(authors)

        document = Document().set_metadata(metadata).set_name_document("../../books/txt/pg" + str(metadata.get_id()) + ".txt")

        return document
