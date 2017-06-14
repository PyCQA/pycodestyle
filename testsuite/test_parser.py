import os
import tempfile
import unittest

import pycodestyle


def _process_file(contents):
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(contents)

    options, args = pycodestyle.process_options(config_file=f.name)
    os.remove(f.name)

    return options, args


class ParserTestCase(unittest.TestCase):

    def test_vanilla_ignore_parsing(self):
        contents = b"""
[pycodestyle]
ignore = E226,E24
        """
        options, args = _process_file(contents)

        self.assertEqual(options.ignore, ["E226", "E24"])

    def test_multiline_ignore_parsing(self):
        contents = b"""
[pycodestyle]
ignore =
    E226,
    E24
        """

        options, args = _process_file(contents)

        self.assertEqual(options.ignore, ["E226", "E24"])

    def test_trailing_comma_ignore_parsing(self):
        contents = b"""
[pycodestyle]
ignore = E226,
        """

        options, args = _process_file(contents)

        self.assertEqual(options.ignore, ["E226"])

    def test_multiline_trailing_comma_ignore_parsing(self):
        contents = b"""
[pycodestyle]
ignore =
    E226,
    E24,
        """

        options, args = _process_file(contents)

        self.assertEqual(options.ignore, ["E226", "E24"])
