import unittest
from __099__two_sum_II import two_sum_II

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual([1, 2], two_sum_II([2, 7, 11, 15], 9))
        self.assertEqual([1,3], two_sum_II([2, 3, 4], 6))
        self.assertEqual([1, 2], two_sum_II([-1, 0], -1))


if __name__ == '__main__':
    unittest.main()