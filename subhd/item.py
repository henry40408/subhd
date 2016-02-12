import requests

from subhd.exceptions import SubHDDownloadException
from subhd.interfaces import ISubHDBase

AJAX_ENDPOINT = "http://subhd.com/ajax/down_ajax"
URL_PATTERN = "http://subhd.com/a/{0}"


class SubHDItem(ISubHDBase):
    def __init__(self, id):
        self.id = int(id)

    def make_url(self):
        return URL_PATTERN.format(self.id)

    def get_file_url(self):
        response = requests.post(AJAX_ENDPOINT, data={"sub_id": self.id})
        url = response.json().get("url")
        if url == "http://dl.subhd.com":
            raise SubHDDownloadException()
        else:
            return url
