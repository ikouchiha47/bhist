import subprocess
import sys
from argparse import ArgumentParser

from .db import create_tables, Bookmarks 
from .read import read_chrome_bookmarks 
from .indexer import create, search_text, show_results

description = '''
Index and search your bookmarks
'''

parser = ArgumentParser(description=description)

parser.add_argument('action', help='action to take', choices=['gather', 'index', 'search'])

parser.add_argument('-c', '--chrome', help='chrome bookmarks file')
parser.add_argument('-ff', '--firefox', help='firefox bookmarks file')
parser.add_argument('-i', '--init', help='first run setup', action='store_true', default=False, required=False)
parser.add_argument('-t', '--term', help='search term', required=False)
parser.add_argument('-f', '--fields', action='append', help='list of fields. allowed. url, name')

args = parser.parse_args(sys.argv[1:])

if 'init' in args and args.init:
    print("setting up tables")
    create_tables()

def gather():
    print("gathering bookmarks")
    bookmarks = read_chrome_bookmarks(args.chrome, Bookmarks.insert)

def index():
    create() 

if args.action == 'gather':
    gather()

if args.action == 'index':
    index()

if args.action == 'search':
    results = search_text(args.term)
    show_results(results, args.fields)