import unittest
from __10__valid_parenthesis import has_valid_parenthesis

class TestValidParenthesis(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(has_valid_parenthesis("()[][][][]{}"))
        self.assertTrue(has_valid_parenthesis('()'))
        self.assertTrue(has_valid_parenthesis(''))


    def test_false_cases(self):
        self.assertFalse(has_valid_parenthesis('()()()[[]'))
        self.assertFalse(has_valid_parenthesis('[][[[[[[[]]]]]]]{'))
        self.assertFalse(has_valid_parenthesis(')))((()))'))


if __name__ == '__main__':
    unittest.main()