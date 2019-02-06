import unittest
import pycodestyle

class ManualTester(unittest.TestCase):
    def test_extraneous_whitespace(self):
        passes = ["spam(ham[1], {eggs: 2})"]
        fails = ["spam( ham[1], {eggs: 2})",
                 "spam(ham[ 1], {eggs: 2})",
                 "spam(ham[1], { eggs: 2})",
                 "spam(ham[1], {eggs: 2} )",
                 "spam(ham[1 ], {eggs: 2})",
                 "spam(ham[1], {eggs: 2 })"
             ]
        
        for case in passes:
            for res in pycodestyle.extraneous_whitespace(case):
                self.assertTrue(res == "")
        
        for case in fails:
            for res in pycodestyle.extraneous_whitespace(case):
                self.assertTrue(res != "")

    def test_whitespace_around_keywords(self):
        passes = [
            "True and False"
        ]

        fails = [
            "True and  False",
            "True  and False",
            "True and\tFalse",
            "True\tand False"
        ]

        test_func = pycodestyle.whitespace_around_keywords

        for case in passes:
            for res in test_func(case):
                self.assertEqual(res, "")

        for case in fails:
            for res in test_func(case):
                self.assertNotEqual(res, "")

    def test_trailing_blank(self):
        passes = ["i=0\n"]
        noNewLine = ["i=0","def foo()"]
        blankLine = [" ", "\n"]
        lines = ["test\n","test\n",passes[0]]
        self.assertEqual(pycodestyle.trailing_blank_lines(passes[0], lines, 3, 3), None)
        lines = ["test\n","test\n",noNewLine[0]]
        self.assertEqual(pycodestyle.trailing_blank_lines(noNewLine[0], lines, 3, 3), (3, 'W292 no newline at end of file'))
        lines = ["test\n","test\n",noNewLine[1]]
        self.assertEqual(pycodestyle.trailing_blank_lines(noNewLine[1], lines, 3, 3), (9, 'W292 no newline at end of file'))
        lines = ["test\n","test\n",blankLine[0]]
        self.assertEqual(pycodestyle.trailing_blank_lines(blankLine[0], lines, 3, 3), (0, 'W391 blank line at end of file'))
        lines = ["test\n","test\n",blankLine[1]]
        self.assertEqual(pycodestyle.trailing_blank_lines(blankLine[1], lines, 3, 3), (0, 'W391 blank line at end of file'))

    def test_trailing_white(self):
        passes = ["i=0\n"]
        fails = ["i=0 "," "]
        self.assertEqual(pycodestyle.trailing_whitespace(passes[0]), None)
        self.assertEqual(pycodestyle.trailing_whitespace(fails[0]), (3, 'W291 trailing whitespace'))
        self.assertEqual(pycodestyle.trailing_whitespace(fails[1]), (0, 'W293 blank line contains whitespace'))

if __name__ == '__main__':
    unittest.main()