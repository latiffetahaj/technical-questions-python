import unittest
from __013__valid_palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome("((123321))"))

    def test_false_cases(self):
        self.assertFalse(is_palindrome("race a car"))
        self.assertFalse(is_palindrome("hello world"))


if __name__ =='__main__':
    unittest.main()