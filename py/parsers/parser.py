from html.parser import HTMLParser
import logging
import re
# from io import StringIO

reject_tag_list = ['head', 'title', 'link', 'style', 'script', 'br', 'template', 'img', 'script', 'iframe']

class Parser:
    def __init__(self):
        self.p = NervousHTMLParser()
        self.data = ""

    def parse(self, s: str):
        try:
            self.p.feed(s)
        except Exception as e:
            print(e)
            self.data = s
        
        return self

    def get_data(self):
        if self.data:
            return self.data
        return self.p.get_data()

class NervousHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.skip = False
        self.data = []

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_starttag(self, tag, attrs):
        if tag in reject_tag_list:
            self.skip = True
            return
        
        self.skip = False

    def handle_endtag(self, tag):
        # print(self.rawdata)
        if tag in reject_tag_list:
            self.skip = False
            return

    def handle_data(self, data):
        if self.skip: return

        data = re.sub('\\\\\w', '', re.sub('\s+',' ',data)).encode("ascii", "ignore").strip().decode('ascii')
        if data != "":
            self.data.append(str(data))

    def get_data(self):
        return ' '.join(self.data)


"""

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_starttag(self, tag, attrs):
        if tag in reject_tag_list:
            self.recording = 0
            return
        logging.debug("start", tag, self.recording)

    def handle_endtag(self, tag):
        if tag in reject_tag_list:
            self.recording = 0
            return

        self.recording = self.recording - 1 if self.recording > 0 else 0
        logging.debug("end", tag, self.recording)
"""
