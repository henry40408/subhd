from subhd.interfaces import ISubHDBase


class SubHDItem(ISubHDBase):
    URL_PATTERN = "http://subhd.com/a/{0}"

    def __init__(self, id):
        self.id = int(id)

    def make_url(self):
        return self.URL_PATTERN.format(self.id)
