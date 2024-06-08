import unittest
from __067__max_sum_subarray import max_sum_subarray

class TestMaxSumSubArray(unittest.TestCase):
    def test_max_sum_subarray(self):
        self.assertEqual(6, max_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]))
        self.assertEqual(23, max_sum_subarray([5,4,-1,7,8]))
        self.assertEqual(1, max_sum_subarray([1]))


if __name__ == '__main__':
    unittest.main()