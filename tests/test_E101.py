"""moved from data files due to 3.12 making this a TokenError"""
import sys
import unittest

from testing.support import errors_from_src


class E101Test(unittest.TestCase):
    def test_E101(self):
        errors = errors_from_src(
            'if True:\n'
            '\tprint(1)  # tabs\n'
            '        print(2)  # spaces\n'
        )
        if sys.version_info >= (3, 12):  # pragma: >=3.12 cover
            self.assertEqual(errors, ['W191:2:1', 'E901:3:28'])
        else:  # pragma: <3.12 cover
            self.assertEqual(errors, ['W191:2:1', 'E101:3:1'])
