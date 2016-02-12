from io import BytesIO

import opencc
import re
import requests

from subhd.archive_handlers import RarHandler
from subhd.exceptions import SubHDDownloadException, SubHDDecompressException
from subhd.utils import SubHDBase, SubtitleFile

AJAX_ENDPOINT = "http://subhd.com/ajax/down_ajax"
CHUNK_SIZE = 2048
URL_PATTERN = "http://subhd.com/a/{0}"


class SubHDSubtitle(SubHDBase):
    def __init__(self, id):
        super(SubHDSubtitle, self).__init__()
        self.id = int(id)
        self.archive_type = None

    def make_url(self):
        return URL_PATTERN.format(self.id)

    def get_file_url(self):
        response = requests.post(AJAX_ENDPOINT, data={"sub_id": self.id})
        url = response.json().get("url")
        if url == "http://dl.subhd.com":
            raise SubHDDownloadException()
        else:
            self.archive_type = url.split(".")[-1].lower()
            return url

    def download_archive(self):
        archive = BytesIO()
        response = requests.get(self.get_file_url())
        for chunk in response.iter_content(CHUNK_SIZE):
            archive.write(chunk)
        archive.seek(0)
        return archive

    def select_handler(self, *, archive):
        if self.archive_type == "rar":
            return RarHandler(archive=archive)
        else:
            return None

    def extract_subtitles(self):
        handler = self.select_handler(archive=self.download_archive())
        if handler:
            return handler.extract_subtitles()
        else:
            message = "Archive type {0} is not yet " \
                      "supported".format(self.archive_type)
            raise SubHDDecompressException(message)

    def translate_subtitles(self):
        subtitles = self.extract_subtitles()
        for index, subtitle in enumerate(subtitles):
            content = subtitle.content.decode("gbk")

            locale = subtitle.filename.split(".")[-2]
            if re.match(r"chs", locale):
                content = opencc.convert(content, config="s2t.json")

            subtitles[index] = SubtitleFile(filename=subtitle.filename,
                                            content=content)
        return subtitles
