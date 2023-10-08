import unittest

from testing.support import errors_from_src


class E231Test(unittest.TestCase):
    def test_E231(self):
        result = errors_from_src("""\
with test(),\\
        test(),     \\
        test():
    pass
""")
        self.assertEqual(result, [])
