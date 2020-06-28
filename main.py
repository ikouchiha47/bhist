import os
import subprocess
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

import firefox
import crawler


with subprocess.Popen(["bash ./firefox/places.sh"], stdout=subprocess.PIPE, shell=True) as proc:
    firefox_files = proc.stdout.read().decode("utf-8").strip().split("\n")

data = firefox.read.call(firefox_files)


def scraper(url):
    crawl = crawler.Crawler()
    return crawl.scrape(url)
 

async def run(executor, data):
    tasks = [
        loop.run_in_executor(executor, scraper, url)
        for profile, urls in data for url, _ in urls[:3]
    ]

    completed, pending = await asyncio.wait(tasks)
    results = [t.result() for t in completed]
    
    return results

executor = ThreadPoolExecutor(6)
loop = asyncio.get_event_loop()

try:
    result = loop.run_until_complete(run(executor, data.items()))
    print(result)
finally:
    loop.close()

