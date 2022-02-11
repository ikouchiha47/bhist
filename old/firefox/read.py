import os
import subprocess
import lib
from firefox import store

# copy sqlite3 dbs because they might be locked
# file name as <profile>_places.sqlite

def __copy(source_file):
    db_with_profile = lambda name: '_'.join(name.split('/')[-2:])

    dest_file="firefox/{}".format(db_with_profile(source_file))
    subprocess.call("cp {source} {dest}".format(source=source_file, dest=dest_file), shell=True)
    return dest_file

def __delete(dest_files):
    for f in dest_files: os.remove(f)

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
    
    history = { db_file: store.urls(db_file) for db_file in dest_db_files }
    
    lib.evt.emit("firefox:dbs:delete", dest_db_files)

    return history

lib.evt.on("firefox:dbs:delete", __delete)

#print(call(sys.argv[1:]))
