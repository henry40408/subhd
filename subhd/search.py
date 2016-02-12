from subhd.subtitle import SubHDSubtitle
from subhd.utils import Entry, SubHDBase

URL_PATTERN = "http://subhd.com/search/{0}"


class SubHDSearch(SubHDBase):
    def __init__(self, *, keyword):
        super(SubHDSearch, self).__init__()
        self.keyword = keyword

    def make_url(self):
        return URL_PATTERN.format(self.keyword)

    def entries(self):
        for entry in self.parse_content().select(".d_title > a"):
            yield Entry(name=entry.text, path=entry["href"])

    def select_subtitle(self, *, choice):
        entries = list(self.entries())
        return SubHDSubtitle(id=entries[choice - 1].path[3:])
