import os
import sys
import sqlite3
import subprocess

# copy sqlite3 dbs because they might be locked
# file name as <profile>_places.sqlite

def __copy(source_file):
    db_with_profile = lambda name: '_'.join(name.split('/')[-2:])

    dest_file="firefox/{}".format(db_with_profile(source_file))
    subprocess.call("cp {source} {dest}".format(source=source_file, dest=dest_file), shell=True)
    return dest_file

def __delete(dest_file):
    os.remove(dest_file)

def __fetch_history(db_file):
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    select_statement = "select url, frecency, last_visit_date from moz_places;"
    cursor.execute(select_statement)

    results = cursor.fetchall()
    
    return[(url, recency, last_visit) for url, recency, last_visit in results]

"""
call(db_files)

copy the sqlite files
read moz_places database and get url and recency
remove the files created
"""

def call(db_files):
    if len(db_files) == 0: {}

    history = {}
    dest_db_files = [__copy(src) for src in db_files]
    
    history = { db_file: __fetch_history(db_file) for db_file in dest_db_files }
    
    for f in dest_db_files: __delete(f)

    return history


print(call(sys.argv[1:]))
