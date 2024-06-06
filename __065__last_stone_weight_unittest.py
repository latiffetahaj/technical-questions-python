import unittest
from __065__last_stone_weight import last_stone_weight

class TestLastStoneWeight(unittest.TestCase):
    def test_last_stone_weight(self):
        self.assertEqual(1, last_stone_weight([1]))
        self.assertEqual(1, last_stone_weight([2,7,4,1,8,1]))
        self.assertEqual(0, last_stone_weight([7,7]))


if __name__ == '__main__':
    unittest.main()