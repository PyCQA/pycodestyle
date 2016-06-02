#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest

from pycodestyle import normalize_paths


class UtilTestCase(unittest.TestCase):
    def test_normalize_paths(self):
        cwd = os.getcwd()

        self.assertEqual(normalize_paths(''), [])
        self.assertEqual(normalize_paths([]), [])
        self.assertEqual(normalize_paths(None), [])
        self.assertEqual(normalize_paths(['foo']), ['foo'])
        self.assertEqual(normalize_paths('foo'), ['foo'])
        self.assertEqual(normalize_paths('foo,bar'), ['foo', 'bar'])
        self.assertEqual(normalize_paths('foo,  bar  '), ['foo', 'bar'])
        self.assertEqual(normalize_paths('/foo/bar,baz/../bat'),
                         ['/foo/bar', cwd + '/bat'])
        self.assertEqual(normalize_paths(".pyc,\n   build/*"),
                         ['.pyc', cwd + '/build/*'])
