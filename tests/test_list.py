import unittest

from subhd.exceptions import SubHDDownloadException
from subhd.interfaces import ISubHDBase
from subhd.list import SubHDList


class TestISubHDBase(unittest.TestCase):
    def test_make_url_not_implemented(self):
        subhd = ISubHDBase()
        self.assertRaises(NotImplementedError, subhd.make_url)


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


if __name__ == "__main__":
    unittest.main()
