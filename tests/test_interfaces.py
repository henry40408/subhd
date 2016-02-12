import unittest

from subhd.interfaces import ISubHDBase


class TestISubHDBase(unittest.TestCase):
    def test_make_url_not_implemented(self):
        subhd = ISubHDBase()
        self.assertRaises(NotImplementedError, subhd.make_url)


if __name__ == "__main__":
    unittest.main()
