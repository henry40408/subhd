import unittest

from subhd.exceptions import SubHDDownloadException
from subhd.list import SubHDList


class TestSubHDList(unittest.TestCase):
    KEYWORD = u"普羅米修斯"

    def setUp(self):
        self.list = SubHDList(keyword=self.KEYWORD)

    def test_parse_content(self):
        document = self.list.parse_content()
        self.assertIn(self.KEYWORD, document.title.text)

    def test_get_content_raises_exception(self):
        self.list.keyword = u"foo/bar"
        self.assertRaises(SubHDDownloadException, self.list.get_content)

    def test_entries(self):
        for entry in self.list.entries():
            self.assertRegex(entry["href"], r"^/a/\d+$")


if __name__ == "__main__":
    unittest.main()
