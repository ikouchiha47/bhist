import xapian

class DbDoc:
    def __init__(self, db, indexers = []):
        self.db = db
        self.indexers = indexers

    def initialize(self):
        self.termgen = xapian.TermGenerator()
        self.termgen.set_stemmer(xapian.Stem("english"))

    def create(self, page):
        doc = xapian.Document()
        self.termgen.set_document(doc)

        self.termgen.index_text(page.title, 1, '#S')
        self.termgen.index_text(page.body, 1, '#D')
        self.termgen.index_text(page.url.path, 1, '#U')
        self.termgen.index_text(page.url.netloc, 1, '#N')

        self.termgen.index_text(page.title)
        self.termgen.increase_termpos()
        self.termgen.index_text(page.body)

        self.db.add_document(doc)
        return True

