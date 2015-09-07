import os
import tempfile
import unittest

import pep8


def _process_file(contents):
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(contents)

    options, args = pep8.process_options(config_file=f.name)
    os.remove(f.name)

    return options, args


class ParserTestCase(unittest.TestCase):

    def test_vanilla_ignore_parsing(self):
        contents = b"""
[pep8]
ignore = E226,E24
        """
        options, args = _process_file(contents)

        self.assertEqual(options.ignore, ["E226", "E24"])

    def test_multiline_ignore_parsing(self):
        contents = b"""
[pep8]
ignore =
    E226,
    E24
        """

        options, args = _process_file(contents)

        self.assertEqual(options.ignore, ["E226", "E24"])

    def test_trailing_comma_ignore_parsing(self):
        contents = b"""
[pep8]
ignore = E226,
        """

        options, args = _process_file(contents)

        self.assertEqual(options.ignore, ["E226"])

    def test_multiline_trailing_comma_ignore_parsing(self):
        contents = b"""
[pep8]
ignore =
    E226,
    E24,
        """

        options, args = _process_file(contents)

        self.assertEqual(options.ignore, ["E226", "E24"])
