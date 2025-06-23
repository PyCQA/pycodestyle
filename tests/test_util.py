import os
import unittest

from pycodestyle import normalize_paths


class UtilTestCase(unittest.TestCase):
    def test_normalize_paths(self):
        self.assertEqual(normalize_paths(''), [])
        self.assertEqual(normalize_paths([]), [])
        self.assertEqual(normalize_paths(None), [])
        self.assertEqual(normalize_paths(['foo']), ['foo'])
        self.assertEqual(normalize_paths('foo'), ['foo'])
        self.assertEqual(normalize_paths('foo,bar'), ['foo', 'bar'])
        self.assertEqual(normalize_paths('foo,  bar  '), ['foo', 'bar'])
        self.assertEqual(
            normalize_paths('/foo/bar,baz/../bat'),
            [os.path.realpath('/foo/bar'), os.path.abspath('bat')],
        )
        self.assertEqual(
            normalize_paths(".pyc,\n   build/*"),
            ['.pyc', os.path.abspath('build/*')],
        )
