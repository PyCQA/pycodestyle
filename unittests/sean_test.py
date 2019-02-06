import unittest
import pycodestyle
class testlines(unittest.TestCase):
    def test_linesize(self):
        s = "mkmmkmkmmkmkmkmkmkmkkkmkmkmkmkmkmkmmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkmkkkmkmkmkmkmkmkm"
        m = "poop"
        assert(len(s) > 79)
        self.assertTrue(pycodestyle.maximum_line_length(s, 79, 0, 0,0))
        assert(len(m) < 79)
        self.assertFalse(pycodestyle.maximum_line_length(m, 79,0,0,0))
    def test_tabs(self):
        g = "wuddlewuddle"
        p = " wuddlewuddle"
        m = ' '
        tab = chr(9)
        h = tab + g
        z = h + p
        assert m == ' '
        self.assertFalse(pycodestyle.tabs_or_spaces(p, m))
        self.assertFalse(pycodestyle.tabs_or_spaces(h, chr(9)))
        self.assertTrue(pycodestyle.tabs_or_spaces(z,m ))

if __name__ == '__main__':
    unittest.main()
