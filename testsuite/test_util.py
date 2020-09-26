#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest

from pycodestyle import normalize_path
from pycodestyle import normalize_paths


class UtilTestCase(unittest.TestCase):
    def test_normalize_path(self):
        cwd = os.getcwd()

        self.assertEqual(normalize_path(''), None)
        self.assertEqual(normalize_path(None), None)
        self.assertEqual(normalize_path('foo'), 'foo')
        self.assertEqual(normalize_path('  bar  '), 'bar')
        self.assertEqual(normalize_path('/foo/bar'), '/foo/bar')
        self.assertEqual(normalize_path('baz/../bat'), cwd + '/bat')
        self.assertEqual(normalize_path("\n   build/*"), cwd + '/build/*')

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
