import unittest

from subhd.interfaces import SubHDBase


class TestSubHDBase(unittest.TestCase):
    def test_make_url_not_implemented(self):
        subhd = SubHDBase()
        self.assertRaises(NotImplementedError, subhd.make_url)


if __name__ == "__main__":
    unittest.main()
