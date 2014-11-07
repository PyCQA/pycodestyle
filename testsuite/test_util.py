#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest

import pep8


class UtilTestCase(unittest.TestCase):
    def test_normalize_paths(self):
        cwd = os.getcwd()

        self.assertEquals(pep8.normalize_paths(''), [])
        self.assertEquals(pep8.normalize_paths(['foo']), ['foo'])
        self.assertEquals(pep8.normalize_paths('foo'), ['foo'])
        self.assertEquals(pep8.normalize_paths('foo,bar'), ['foo', 'bar'])
        self.assertEquals(pep8.normalize_paths('/foo/bar,baz/../bat'),
                          ['/foo/bar', cwd + '/bat'])
        self.assertEquals(pep8.normalize_paths(".pyc,\n   build/*"),
                          ['.pyc', cwd + '/build/*'])
