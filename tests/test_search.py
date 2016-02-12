import unittest

from subhd.exceptions import SubHDDownloadException
from subhd.search import SubHDSearch


class TestSearch(unittest.TestCase):
    KEYWORD = u"普羅米修斯"

    def setUp(self):
        self.search = SubHDSearch(keyword=self.KEYWORD)

    def test_parse_content(self):
        document = self.search.parse_content()
        self.assertIn(self.KEYWORD, document.title.text)

    def test_get_content_raises_exception(self):
        self.search.keyword = u"foo/bar"
        self.assertRaises(SubHDDownloadException, self.search.get_content)

    def test_entries(self):
        for entry in self.search.entries():
            self.assertRegex(entry["href"], r"^/a/\d+$")


if __name__ == "__main__":
    unittest.main()
