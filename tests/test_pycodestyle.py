import io
import sys
import tokenize

import pytest

from pycodestyle import Checker
from pycodestyle import expand_indent
from pycodestyle import mute_string


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('    ', 4),
        ('\t', 8),
        ('       \t', 8),
        ('        \t', 16),
    ),
)
def test_expand_indent(s, expected):
    assert expand_indent(s) == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('"abc"', '"xxx"'),
        ("'''abc'''", "'''xxx'''"),
        ("r'abc'", "r'xxx'"),
    ),
)
def test_mute_string(s, expected):
    assert mute_string(s) == expected


def test_fstring_logical_line():
    src = '''\
f'hello {{ {thing} }} world'
'''
    checker = Checker(lines=src.splitlines())
    checker.tokens = list(tokenize.generate_tokens(io.StringIO(src).readline))
    checker.build_tokens_line()

    if sys.version_info >= (3, 12):  # pragma: >3.12 cover
        assert checker.logical_line == "f'xxxxxxxxx{thing}xxxxxxxxx'"
    else:
        assert checker.logical_line == "f'xxxxxxxxxxxxxxxxxxxxxxxxx'"
