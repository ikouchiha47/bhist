import xapian
import os
import subprocess
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

import firefox
import crawler
import dbdoc

with subprocess.Popen(["bash ./firefox/places.sh"], stdout=subprocess.PIPE, shell=True) as proc:
    firefox_files = proc.stdout.read().decode("utf-8").strip().split("\n")

data = firefox.read.call(firefox_files)


def scraper(url):
    crawl = crawler.Crawler()
    return crawl.scrape(url)


def indexer(d, result):
    d.create(result)

async def run(executor, data, d):
    tasks = [
        loop.run_in_executor(executor, scraper, url)
        for profile, urls in data for url, _ in urls[:3]
    ]

    completed, pending = await asyncio.wait(tasks)
    results = [t.result() for t in completed]

    for result in results:
        d.create(result)

    return results

executor = ThreadPoolExecutor(6)
loop = asyncio.get_event_loop()

try:
    db = xapian.WritableDatabase("./db", xapian.DB_CREATE_OR_OPEN)
    d = dbdoc.DbDoc(db)
    d.initialize()

    results = loop.run_until_complete(run(executor, data.items(), d))
    print(results)
finally:
    loop.close()

