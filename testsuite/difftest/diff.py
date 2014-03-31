import os
import re
import os.path
from fnmatch import fnmatch

HUNK_REGEX = re.compile(r'^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@.*$')


def filename_match(filename, patterns, default=True):
    """
    Check if patterns contains a pattern that matches filename.
    If patterns is unspecified, this always returns True.
    """
    if not patterns:
        return default
    return any(fnmatch(filename, pattern) for pattern in patterns)


def parse_udiff_sub(paragraph, patterns, parent):
    rv = {}
    lineCount = 0
    path = nrows = None

    for line in paragraph.splitlines():
        lineCount += 1

        if nrows:
            if line[:1] == '-':
                lineCount -= 1
            elif line[:1] == '+':
                rv[path].add(lineCount)

        if line[:3] == '@@ ':
            hunk_match = HUNK_REGEX.match(line)
            row, nrows = [int(g or '1') for g in hunk_match.groups()]
            lineCount = row - 1
        elif line[:3] == '+++':
            path = line[4:].split('\t', 1)[0]
            if path[:2] == 'b/':
                path = path[2:]
            rv[path] = set()

    for (path, rows) in rv.items():
        if rows and filename_match(path, patterns):
            return (os.path.join(parent, path), rows)


def parse_udiff(diff, patterns=None, parent='.'):
    test = []

    for para in diff.split('diff --git '):
        diff = parse_udiff_sub(para, patterns, parent)
        if diff:
            test.append(diff)
    return dict(test)


if __name__ == '__main__':
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            fileHandle = open(f)
            text = fileHandle.read()
            dic = parse_udiff(text)
            print f
            print dic
            print '>>>>>>>>>>>>>>>>>>'
