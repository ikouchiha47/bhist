import sqlite3
import os
import subprocess
import uuid
import asyncio

from typing import List
from concurrent.futures.thread import ThreadPoolExecutor

from py.models.bookmark import Bookmark
from py.cmd import chrome
from py.utils import chunker, run, flatten

from .queries import urls


class Firefox:
    def __init__(self, dbpath, parser):
        self.dbpath = dbpath
        self.parser = parser
        self.executable = chrome()

    def get_bookmarks(self, handler) -> List[Bookmark]:
        records = urls(self.dbpath)
        bookmarks = self.__get_bookmark_objects__(records)

        executor = ThreadPoolExecutor(6)
        loop = asyncio.get_event_loop()
       
        results = loop.run_until_complete(
                run(executor, loop, chunker(bookmarks, 6), self.__process_bookmarks__))

        res = flatten(results)
        try:
            handler(res)
        except Exception as e:
            print(e)

        return res

        # return self.__process_bookmarks__(bookmarks)

    def __get_bookmark_objects__(self, records):
        bookmarks = []

        for obj in records:
            _id = uuid.uuid4().hex
            bookmark = Bookmark(
                        url=obj[0],
                        name=obj[1],
                        id_type="uid",
                        _id=_id,
                        date_added=obj[2]
                    )
            bookmarks.append(bookmark)

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


