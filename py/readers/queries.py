import sqlite3

select_places_history="""
SELECT
    url, last_visit_date
FROM 
    moz_places
ORDER BY frecency;"""

select_places_bookmarks="""
SELECT
    moz_places.url as url,
    moz_bookmarks.title as title,
    moz_places.last_visit_date as last_visit_date,
    moz_bookmarks.dateAdded as date_added
FROM
    moz_places
INNER JOIN
    moz_bookmarks ON moz_bookmarks.fk=moz_places.id
ORDER BY moz_places.frecency;"""

def urls(db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    cursor.execute(select_places_bookmarks)

    results = cursor.fetchall()
    
    return[(url, title, date_added, last_visit) for url, title, last_visit, date_added in results]

