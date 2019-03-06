import unittest
import pycodestyle

class AutomatedTester(unittest.TestCase):
    def test_is_binary_operator(self):
        passes = ["and","or"]
        fails = "()[]{},:.;@=%~"

        for case in passes:
            response = pycodestyle._is_binary_operator(None, case)
            self.assertTrue(response)
        
        for case in fails:
            response = pycodestyle._is_binary_operator(None, case)
            self.assertFalse(response)

    def test_comparison_negative(self):
        passes = [
            "Okay: if x not in y:\n    pass",
            "Okay: assert (X in Y or X is Z)",
            "Okay: if not (X in Y):\n    pass",
            "Okay: zz = x is not y"
        ]
        
        fails = [
            "E713: Z = not X in Y",
            "E713: if not X.B in Y:\n    pass",
            "E714: if not X is Y:\n    pass",
            "E714: Z = not X.B is Y"
        ]

        for case in passes:
            for response in pycodestyle.comparison_negative(case):
                self.assertEqual(response, "")

        for case in fails:
            for response in pycodestyle.comparison_negative(case):
                self.assertTrue("E713" in response[1] or "E714" in response[1])
                
if __name__ == '__main__':
    unittest.main()