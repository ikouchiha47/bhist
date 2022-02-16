import itertools
import asyncio
from urllib.parse import urlparse
from pathlib import Path

__skip_list__ = ["figma", "pdf", "jpg", "png"]

def is_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def flatten(arr):
    return list(itertools.chain.from_iterable(arr))

def chunker(seq, size = 6):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


async def run(executor, looper, groups, method, *args):
    tasks = [
            looper.run_in_executor(executor, method, *args, data)
            for data in groups
            ]

    completed, pending = await asyncio.wait(tasks)
    results = [t.result() for t in completed]
    return results
 

def should_skip(url):
    for skip in __skip_list__:
        if skip in url:
            return True
    return False


def __hydrate__skiplist__():
    __f__ = Path(".bsignore")

    if __f__.is_file():
        with open('.bignore') as f:
            for line in f.readlines():
                __skip_list__.append(line)


__hydrate__skiplist__()
