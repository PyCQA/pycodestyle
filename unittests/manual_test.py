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

if __name__ == '__main__':
    unittest.main()