import unittest
from __058__palindromic_substring import count_palindromic_substrings

class TestPalindromicSubstrings(unittest.TestCase):

    def test_palindromic_substrings(self):
        self.assertEqual(3, count_palindromic_substrings('abc'))
        self.assertEqual(6, count_palindromic_substrings('aaa'))
        self.assertEqual(1, count_palindromic_substrings('a'))


if __name__ == '__main__':
    unittest.main()