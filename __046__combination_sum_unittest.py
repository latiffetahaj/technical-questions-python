import unittest
from __046__combination_sum import combination_sum


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum(self):
        self.assertEqual([[2,2,3],[7]], combination_sum([2,3,6,7],7))

        self.assertEqual([],combination_sum([12,14,15], 3))

        self.assertEqual([[2,2,2,2],[2,3,3],[3,5]], combination_sum([2,3,5],8))


if __name__ == '__main__':
    unittest.main()