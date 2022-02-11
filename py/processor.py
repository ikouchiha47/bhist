# import subprocess
# import os
# import pdb
# from typing import List
# from multiprocessing import Process, Pool

# from .cmd import chrome
# from .model import Bookmark
# from .parser import NervousHTMLParser

# def get_text_from_url(url: str) -> str :
    # print(url)
    # command = [
            # chrome(),
            # '--headless',
            # '--disable-gpu',
            # '--crash-dumps-dir=/tmp',
            # '--dump-dom'
            # ]
    # command = ' '.join(command)
    # p = subprocess.Popen(f'{command} "{url}"', shell=True, stdout=subprocess.PIPE, executable=os.environ['SHELL'])
    # contents = p.communicate()[0]

    # parser = NervousHTMLParser()
    # import pdb; pdb.set_trace()
    # parser.feed(str(contents))

    # print(str(parser.get_data()))
    # print("=====================")

    # return parser.get_data()

# def process_bookmarks(bookmarks: List[Bookmark], callback) -> List[Bookmark]:
    # result = []

    # with Pool(5) as pool:
        # grouped_bookmarks = chunker(bookmarks, 5)

        # for books in grouped_bookmarks:
            # b = pool.apply_async(__process_bookmark__, (books, callback,)).get()
            # result.extend(result)

    # return result

# def __process_bookmark__(bookmarks: List[Bookmark], callback):
    # print(bookmarks)
    # for book in bookmarks:
        # book.content = get_text_from_url(book.url)
        # callback(book)
    # return bookmarks


# def chunker(seq, size):
    # return (seq[pos:pos + size] for pos in range(0, len(seq), size))
