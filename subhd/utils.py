from collections import namedtuple

import requests
from bs4 import BeautifulSoup

from subhd.exceptions import SubHDDownloadException

SubtitleFile = namedtuple("SubtitleFile", ["filename", "content"])
Entry = namedtuple("Entry", ["name", "path"])


class SubHDBase(object):
    def __init__(self):
        self.content = None

    def make_url(self):
        raise NotImplementedError()

    def get_content(self):
        if not self.content:
            response = requests.get(self.make_url())
            if response.status_code == 200:
                self.content = response.text
            else:
                raise SubHDDownloadException()
        return self.content

    def parse_content(self):
        return BeautifulSoup(self.get_content(), "html.parser")