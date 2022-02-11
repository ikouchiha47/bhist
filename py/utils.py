from urllib.parse import urlparse
from pathlib import Path

__skip_list__ = ["figma", "pdf", "jpg", "png"]

def is_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

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
