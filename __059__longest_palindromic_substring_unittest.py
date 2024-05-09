import unittest
from __059__longest_palindromic_substring import longest_palindromic_substring

class TestLongestPalindromicSubstring(unittest.TestCase):

    def test_longest_palindromic_substring(self):
        self.assertEqual('bab', longest_palindromic_substring('babad'))
        self.assertEqual('bb', longest_palindromic_substring('cbbd'))
        self.assertEqual('', longest_palindromic_substring(''))


if __name__ == '__main__':
    unittest.main()