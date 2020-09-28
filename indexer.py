from collections import defaultdict
import xapian

class Indexer:
    def __init__(self):
        self.indexers = defaultdict(list)

    def register(self, name, fn):
        self.indexers[name].append(fn)

    def run(self, name):
        if len(self.indexers[name]) == 0:
            return True

        for fn in self.indexers[name]:
            res = fn()
            if not res: return False

        return True


# idxr = Indexer("./db")
# idxr.initialize()

