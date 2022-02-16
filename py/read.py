import json

from .db import Bookmarks

from py.readers.chrome import Chrome
from py.readers.firefox import Firefox
from py.parsers.parser import Parser


def read_chrome_bookmarks(filename: str):
    ch = Chrome(filename, Parser())
    bookmarks = ch.get_bookmarks(Bookmarks.insert_bulk)
    print(bookmarks)
    # Bookmarks.insert_bulk(bookmarks)

def read_firefox_bookmarks(dbpath: str):
    print("firefox bookmarks")
    ff = Firefox(dbpath, Parser())
    bookmarks = ff.get_bookmarks(Bookmarks.insert_bulk)

    print(bookmarks)
    # Bookmarks.insert_bulk(bookmarks)

