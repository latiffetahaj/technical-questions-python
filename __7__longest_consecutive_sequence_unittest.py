import unittest
from __7__longest_consecutive_sequence import longest_sequence

class TestLongestSequence(unittest.TestCase):
    def test_positive_nums(self):
        self.assertEqual(9, longest_sequence([0,3,7,2,5,8,4,6,0,1]))
        self.assertEqual(4, longest_sequence([100,3,200,1,4,2]))

    def test_negative_nums(self):
        self.assertEqual(4,longest_sequence([9,-2,6,13,-4,2,1,-1,-3]))

    def test_empty(self):
        self.assertEqual(0,longest_sequence([]))

    def test_null(self):
        self.assertEqual(0,longest_sequence(None))




if __name__ == '__main__':
    unittest.main()