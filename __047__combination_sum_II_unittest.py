import unittest
from __047__combination_sum_II import combination_sum_II

class TestCombinationSumII(unittest.TestCase):
    def test_combination_sum_II(self):
        self.assertEqual([[1,1,6], [1,2,5], [1,7], [2,6]], combination_sum_II([10,1,2,7,6,1,5], 8))

        self.assertEqual([[1,2,2], [5]], combination_sum_II([2, 5, 2, 1, 2], 5))



if __name__ == '__main__':
    unittest.main()