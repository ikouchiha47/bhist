from typing import List

from py.models.bookmark import Bookmark

class Firefox:
    def __init__(self, filename, parser):
        self.filename = filename
        self.parser = parser

    def get_bookmarks(self) -> List[Bookmark]:
        pass
