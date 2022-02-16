import xapian
import json
from typing import List

from .db import Bookmarks
from py.models.bookmark import Bookmark

xdb = xapian.WritableDatabase('bookmarks_xapian', xapian.DB_CREATE_OR_OPEN)

def create():
    termgenerator = xapian.TermGenerator()
    termgenerator.set_stemmer(xapian.Stem("en"))
    
    bookmarks, offset = Bookmarks.fetch(0)
    while offset > 0:
        __index_bookmarks__(termgenerator, bookmarks)
        bookmarks, offset = Bookmarks.fetch(offset)


def search_text(text):
    enquire = xapian.Enquire(xdb)
    text = ' '.join(text.split())

    qp = xapian.QueryParser()
    stemmer = xapian.Stem("en")
    qp.set_stemmer(stemmer)

    qp.set_database(xdb)
    qp.set_stemming_strategy(xapian.QueryParser.STEM_SOME)

    query = qp.parse_query(text)
    # print("Parsed query is: %s" % str(query))

    # Find the top 10 results for the query.
    enquire.set_query(query)
    matches = enquire.get_mset(0, 10)

    # Display the results.
    print("%i results found." % matches.get_matches_estimated())
    print("Results 1-%i:" % matches.size())
    return matches

def show_results(matches: List, filter_keys = []):
    for m in matches:
        data = m.document.get_data()
        if not data: continue

        obj = json.loads(data)

        if len(filter_keys) == 0:
            print(data)
            continue

        for key in filter_keys:
            print(obj[key])


def __index_bookmarks__(termgen, bookmarks: List[Bookmark]):
    for bookm in bookmarks:
        __index_bookmark__(termgen, bookm)


def __index_bookmark__(termgen, bookmark: Bookmark):
    doc = xapian.Document()

    termgen.set_document(doc)
    termgen.index_text(bookmark.content, 1, 'S')
    termgen.index_text(bookmark.name, 1, 'S')

    termgen.index_text(bookmark.name)
    termgen.increase_termpos()
    termgen.index_text(bookmark.content)

    doc.set_data(bookmark.url)
    doc.set_data(bookmark.name)
    doc.set_data(json.dumps(bookmark.__dict__))

    idterm = u"Q" + f'{bookmark.id_type}_{bookmark._id}'
    doc.add_boolean_term(idterm)
    xdb.replace_document(idterm, doc)


