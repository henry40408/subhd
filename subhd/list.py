from subhd.interfaces import ISubHDBase


class SubHDList(ISubHDBase):
    URL_PATTERN = "http://subhd.com/search/{0}"

    def __init__(self, *, keyword):
        self.keyword = keyword

    def make_url(self):
        return self.URL_PATTERN.format(self.keyword)

    def entries(self):
        for entry in self.parse_content().select(".d_title > a"):
            yield entry
