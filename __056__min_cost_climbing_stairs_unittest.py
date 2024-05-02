import unittest
from __056__min_cost_climbing_stairs import min_cost_climbing

class TestMinCostClimbingStairs(unittest.TestCase):

    def test_min_cost(self):
        self.assertEqual(15, min_cost_climbing([10,15,20]))
        self.assertEqual(6, min_cost_climbing([1,100,1,1,1,100,1,1,100,1]))


if __name__ == '__main__':
    unittest.main()