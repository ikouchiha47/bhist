import datetime as dt

class Bookmark(object):
    def __init__(self, url: str, name: str, id_type: str, _id: str, date_added: int, content = ''):
        self.url = url
        self.content = content
        self.name = name
        self.id_type = id_type
        self._id = _id
        self.date_added = date_added
        self.last_updated_at = int(dt.datetime.now().replace(microsecond=0).timestamp())
