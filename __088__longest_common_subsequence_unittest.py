import unittest
from __088__longest_common_subsequence import longest_common_subsequence, longest_common_subsequence_II

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_longest_common_subsequence(self):
        self.assertEqual(3, longest_common_subsequence("abcde", "ace"))
        self.assertEqual(0, longest_common_subsequence("ae", "c"))
        self.assertEqual(4, longest_common_subsequence("abcd", "abcd"))

    def test_longest_common_subsequence_II(self):
        self.assertEqual(3, longest_common_subsequence_II("abcde", "ace"))
        self.assertEqual(0, longest_common_subsequence_II("ae", "c"))
        self.assertEqual(4, longest_common_subsequence_II("abcd", "abcd"))



if __name__ == '__main__':
    unittest.main()

