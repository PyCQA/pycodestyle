#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest

import pep8


class UtilTestCase(unittest.TestCase):
    def test_normalize_paths(self):
        cwd = os.getcwd()

        self.assertEqual(pep8.normalize_paths(''), [])
        self.assertEqual(pep8.normalize_paths([]), [])
        self.assertEqual(pep8.normalize_paths(None), [])
        self.assertEqual(pep8.normalize_paths(['foo']), ['foo'])
        self.assertEqual(pep8.normalize_paths('foo'), ['foo'])
        self.assertEqual(pep8.normalize_paths('foo,bar'), ['foo', 'bar'])
        self.assertEqual(pep8.normalize_paths('foo,  bar  '), ['foo', 'bar'])
        self.assertEqual(pep8.normalize_paths('/foo/bar,baz/../bat'),
                         ['/foo/bar', cwd + '/bat'])
        self.assertEqual(pep8.normalize_paths(".pyc,\n   build/*"),
                         ['.pyc', cwd + '/build/*'])
