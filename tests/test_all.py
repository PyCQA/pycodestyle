import os.path

import pycodestyle
from testing.support import ROOT


def test_own_dog_food():
    style = pycodestyle.StyleGuide(select='E,W', quiet=True)
    files = [pycodestyle.__file__, __file__, os.path.join(ROOT, 'setup.py')]
    report = style.init_report(pycodestyle.StandardReport)
    report = style.check_files(files)
    assert list(report.messages) == ['W504'], f'Failures: {report.messages}'
