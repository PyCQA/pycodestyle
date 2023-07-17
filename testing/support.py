from __future__ import annotations

from pycodestyle import BaseReport
from pycodestyle import StyleGuide


class InMemoryReport(BaseReport):
    """
    Collect the results in memory, without printing anything.
    """

    def __init__(self, options):
        super().__init__(options)
        self.in_memory_errors = []

    def error(self, line_number, offset, text, check):
        """
        Report an error, according to options.
        """
        code = text[:4]
        self.in_memory_errors.append(f'{code}:{line_number}:{offset + 1}')
        return super().error(line_number, offset, text, check)


def errors_from_src(src: str) -> list[str]:
    guide = StyleGuide(select=('E', 'W'))
    reporter = guide.init_report(InMemoryReport)
    guide.input_file(
        filename='in-memory-test-file.py',
        lines=src.splitlines(True),
    )
    return reporter.in_memory_errors
