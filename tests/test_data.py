from __future__ import annotations

import collections
import os.path
import re
import sys

import pytest

import pycodestyle
from testing.support import errors_from_src
from testing.support import ROOT

PY_RE = re.compile(r'^python(\d)(\d*)\.py$')
CASE_RE = re.compile('^(#:.*\n)', re.MULTILINE)


def _nsort(items: list[str]) -> list[str]:
    return sorted(
        items,
        key=lambda s: [
            int(part) if part.isdigit() else part.lower()
            for part in re.split(r'(\d+)', s)
        ],
    )


def get_tests():
    ret = []
    for fname in _nsort(os.listdir(os.path.join(ROOT, 'testing', 'data'))):
        match = PY_RE.match(fname)
        if match is not None:
            major, minor = int(match[1]), int(match[2] or '0')
            mark = pytest.mark.skipif(
                sys.version_info < (major, minor),
                reason=f'requires Python {major}.{minor}',
            )
        else:
            mark = ()

        fname = os.path.join('testing', 'data', fname)
        fname_full = os.path.join(ROOT, fname)
        src = ''.join(pycodestyle.readlines(fname_full))

        line = 1
        parts_it = iter(CASE_RE.split(src))
        # the first case will not have a comment for it
        s = next(parts_it)
        if s.strip():
            id_s = f'{fname}:{line}'
            ret.append(pytest.param('#: Okay', s, id=id_s, marks=mark))
            line += s.count('\n')

        for comment, s in zip(parts_it, parts_it):
            if s.strip():
                id_s = f'{fname}:{line}'
                ret.append(pytest.param(comment, s, id=id_s, marks=mark))
                line += s.count('\n') + 1

    assert ret
    return ret


@pytest.mark.parametrize(('case', 's'), get_tests())
def test(case, s):
    codes = collections.Counter()
    exact = collections.Counter()

    assert case.startswith('#:')
    for code in case[2:].strip().split():
        if code == 'Okay':
            continue
        elif code == 'noeol':
            s = s.rstrip('\n')
        elif ':' in code:
            exact[code] += 1
        else:
            codes[code] += 1

    unexpected = collections.Counter()
    for code in errors_from_src(s):
        if exact[code]:
            exact[code] -= 1
        elif codes[code[:4]]:
            codes[code[:4]] -= 1
        else:  # pragma: no cover
            unexpected[code] += 1

    messages = (
        *(f'-{k}\n' for k, v in codes.items() for _ in range(v)),
        *(f'-{k}\n' for k, v in exact.items() for _ in range(v)),
        *(f'+{k}\n' for k, v in unexpected.items() for _ in range(v)),
    )
    if messages:  # pragma: no cover
        raise AssertionError(f'unexpected codes!\n{"".join(messages)}')
