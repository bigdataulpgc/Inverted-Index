from datetime import datetime


class Metadata:

    def __init__(self):
        self._id = None
        self._authors = []
        self._title = None
        self._release_date = None
        self._posting_date = None
        self._language = None

    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id
        return self

    def get_authors(self):
        return self._authors

    def add_authors(self, new_author):
        if new_author != "None":
            self._authors.append(new_author)
        return self

    def get_title(self):
        return self._title

    def set_title(self, new_title):
        if new_title != "None":
            self._title = new_title
        return self

    def get_release_date(self):
        return self._release_date

    def set_release_date(self, new_release_date):
        if new_release_date != "None":
            self._release_date = datetime.strptime(new_release_date, "%d-%m-%Y").strftime("%d-%m-%Y")
        return self

    def get_posting_date(self):
        return self._posting_date

    def set_posting_date(self, new_posting_date):
        if new_posting_date != "None":
            self._posting_date = datetime.strptime(new_posting_date, "%d-%m-%Y").strftime("%d-%m-%Y")
        return self

    def get_language(self):
        return self._language

    def set_language(self, new_language):
        if new_language != "None":
            self._language = new_language
        return self
