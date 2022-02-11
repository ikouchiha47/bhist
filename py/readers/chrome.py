import subprocess
import os
import json
from typing import List

from py.models.bookmark import Bookmark
from py.utils import is_url, should_skip
from py.cmd import chrome

class Chrome:
    def __init__(self, filename, parser):
        self.filename = filename
        self.parser = parser
        self.executable = chrome()

    def get_bookmarks(self) -> List[Bookmark]:
        with open(self.filename, mode='r', encoding='utf-8') as f:
            jsonstr = f.read().strip()

        bookmarks = self.__get_bookmark_objects__(json.loads(jsonstr))
        return self.__process_bookmarks__(bookmarks)

    def __get_bookmark_objects__(self, bms):
        root = bms["roots"]
        bookmarks = []
    
        for key in root.keys():
            books = root[key]["children"]
            for bm in books:
                if not is_url(bm["url"]): continue
                if should_skip(bm["url"]): continue

                bk = Bookmark(
                        url=bm["url"],
                        name=bm["name"],
                        id_type="guid",
                        _id=bm["guid"],
                        date_added=bm["date_added"]
                    )
                bookmarks.append(bk)

        return bookmarks

    def __process_bookmarks__(self, bookmarks: List[Bookmark]) -> List[Bookmark]:
        for book in bookmarks:
            book.content = self.__get_text_from_url__(book.url)
        return bookmarks

    def __get_text_from_url__(self, url: str) -> str:
        print(url)
        command = [
            self.executable,
            '--headless',
            '--disable-gpu',
            '--crash-dumps-dir=/tmp',
            '--dump-dom'
            ]
        command = ' '.join(command)
        p = subprocess.Popen(
                f'{command} "{url}"',
                shell=True,
                stdout=subprocess.PIPE,
                executable=os.environ['SHELL'])
        contents = p.communicate()[0]

        # import pdb; pdb.set_trace()
        # return parser.get_data()
        return self.parser.parse(str(contents)).get_data()



def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
