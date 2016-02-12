import unittest

import opencc

from subhd.item import SubHDItem


class TestItem(unittest.TestCase):
    KEYWORD = u"普羅米修斯"
    ID = 309312

    def setUp(self):
        self.item = SubHDItem(self.ID)

    def test_parse_content(self):
        document = self.item.parse_content()
        converted_keyword = opencc.convert(self.KEYWORD, config="t2s.json")
        self.assertIn(converted_keyword, document.title.text)


if __name__ == "__main__":
    unittest.main()
