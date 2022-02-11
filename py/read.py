import json
from typing import List, Dict
from urllib.parse import urlparse
from pathlib import Path

from .model import Bookmark
from .processor import process_bookmarks

skip_list = ["figma", "pdf", "jpg", "png"]

f = Path(".bsignore")
if f.is_file():
    with open('.bignore') as f:
        for line in f.readlines():
            skip_list.append(line)

def read_chrome_bookmarks(filename: str, callback):
    bookmarks = read_bookmarks(filename)
    return process_bookmarks(get_bookmark_objects(bookmarks), callback)


def read_firefox_bookmarks():
    print("firefox bookmarks")


def read_bookmarks(filename: str):
    with open(filename, 'r') as f:
        jsonstr = f.read().strip()

    return json.loads(jsonstr)

def get_bookmark_objects(bms):
    root = bms["roots"]
    bookmarks = []
    
    for key in root.keys():
        books = root[key]["children"]
        for bm in books:
            if not is_url(bm["url"]): continue
            if should_skip(bm["url"]): continue

            bk = Bookmark(url=bm["url"], name=bm["name"], id_type="guid", _id=bm["guid"], date_added=bm["date_added"])
            bookmarks.append(bk)

    return bookmarks

def is_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def should_skip(url):
    for skip in skip_list:
        if skip in url:
            return True
    return False
