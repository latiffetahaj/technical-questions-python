import unittest
from __053__house_robber_II import rob_houses_II

class TestRobHousesII(unittest.TestCase):

    def test_rob_houses_II(self):
        self.assertEqual(3, rob_houses_II([2,3,2]))

        self.assertEqual(4, rob_houses_II([1,2,3,1]))

        self.assertEqual(5, rob_houses_II([5]))


if __name__ == '__main__':
    unittest.main()