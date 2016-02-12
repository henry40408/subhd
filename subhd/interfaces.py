import requests
from bs4 import BeautifulSoup

from subhd.exceptions import SubHDDownloadException


class SubHDBase(object):
    def make_url(self):
        raise NotImplementedError()

    def get_content(self):
        response = requests.get(self.make_url())
        if response.status_code == 200:
            return response.text
        else:
            raise SubHDDownloadException()

    def parse_content(self):
        return BeautifulSoup(self.get_content(), "html.parser")


class IArchiveHandler(object):
    def __init__(self, *, archive):
        self.archive = archive

    def iter_files(self):
        raise NotImplementedError()

    def extract_subtitles(self):
        subtitles = []
        for subtitle_file in self.iter_files():
            subtitles.append(subtitle_file)
        return subtitles
