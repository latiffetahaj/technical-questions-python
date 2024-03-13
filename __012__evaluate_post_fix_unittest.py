import unittest
from __012__evaluate_post_fix import evaluate_post_fix

class TestEvaluatePostFix(unittest.TestCase):
    def test(self):
        self.assertEqual(9,evaluate_post_fix(["2","1","+","3","*"]))
        self.assertEqual(22,evaluate_post_fix(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
        self.assertEqual(5,evaluate_post_fix(["2", "3", "+"]))


if __name__ == '__main__':
    unittest.main()
