import unittest
from __021__longest_substring import length_longest_substring

class TestLongestSubstring(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(0,length_longest_substring(""))

    def test_small_inputs(self):
        self.assertEqual(1,length_longest_substring("a"))
        self.assertEqual(1,length_longest_substring("aaa"))
        self.assertEqual(2,length_longest_substring("ab"))
        self.assertEqual(3,length_longest_substring("dvdf"))

    def test_regular_cases(self):
        self.assertEqual(5,length_longest_substring("abcdec"))
        self.assertEqual(3,length_longest_substring("pwwkew"))


if __name__ == '__main__':
    unittest.main()