from subhd.interfaces import ISubHDBase

URL_PATTERN = "http://subhd.com/search/{0}"


class SubHDList(ISubHDBase):
    def __init__(self, *, keyword):
        self.keyword = keyword

    def make_url(self):
        return URL_PATTERN.format(self.keyword)

    def entries(self):
        for entry in self.parse_content().select(".d_title > a"):
            yield entry
