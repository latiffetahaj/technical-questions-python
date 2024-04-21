import unittest
from __054__longest_increasing_subsequence import length_of_LIS

class TestLengthLIS(unittest.TestCase):

    def test_length_of_LIS(self):
        self.assertEqual(4, length_of_LIS([10,9,2,5,3,7,101,18]))

        self.assertEqual(1, length_of_LIS([7,7,7,7]))

        self.assertEqual(3, length_of_LIS([-1, -5, 0, 6, 3]))



if __name__ == '__main__':
    unittest.main()