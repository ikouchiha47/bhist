import sqlite3
from typing import List

from py.models.bookmark import Bookmark

limit = 20
connection = sqlite3.connect("bookmarks_search.db")

def create_tables():
    cur = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS bookmarks(
            url text not null,
            name text,
            content text,
            uid_type varchar(255),
            uid_id varchar(255),
            last_updated_at timestamp not null,
            date_added timestamp not null
    )''')
    connection.commit()


class Bookmarks:
    con = connection

    @classmethod
    def insert(self, bookmark: Bookmark):
        cur = self.con.cursor()
        cur.execute("""INSERT INTO bookmarks(
            url,
            name,
            content,
            uid_type,
            uid_id,
            date_added,
            last_updated_at) VALUES (?,?,?,?,?,?,?)
        """, (bookmark.url, bookmark.name, bookmark.content, bookmark.id_type, bookmark._id, bookmark.date_added, bookmark.last_updated_at))
        self.con.commit()

    @classmethod
    def insert_bulk(self, bookmarks: List[Bookmark]):
        data = [(b.url, b.name, b.content, b.id_type, b._id, b.date_added, b.last_updated_at) for b in bookmarks]

        cur = self.con.cursor()
        cur.executemany("""INSERT INTO bookmarks(
            url,
            name,
            content,
            uid_type,
            uid_id,
            date_added,
            last_updated_at) VALUES (?,?,?,?,?,?,?)
        """, data)
        
        self.con.commit()

    @classmethod
    def fetch(self, offset: int) -> (List[Bookmark], int) :
        cur = self.con.cursor()

        cur.execute('SELECT COUNT(1) FROM bookmarks')
        count = cur.fetchone()[0]

        print("count ", count, " offset ", offset)
        
        if offset > count:
            return [], -1

        bookmarks = []
        for row in cur.execute(f'''SELECT
                                    url,
                                    name,
                                    content,
                                    uid_type,
                                    uid_id,
                                    date_added,
                                    last_updated_at
                                  FROM
                                    bookmarks
                                  LIMIT {limit} OFFSET {offset}'''):
            bookmark = Bookmark(
                    url=row[0],
                    name=row[1],
                    id_type=row[3],
                    _id=row[4],
                    date_added=row[5],
                    content=row[2])
            bookmark.last_updated_at = row[6]
            bookmarks.append(bookmark)

        self.con.commit()
        return bookmarks, offset+limit

