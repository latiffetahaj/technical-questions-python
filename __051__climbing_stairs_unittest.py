import unittest
from __051__climbing_stairs import climbing_stairs

class TestClimbingStairs(unittest.TestCase):

    def test_climbing_stairs(self):
        self.assertEqual(1,climbing_stairs(1))
        self.assertEqual(2,climbing_stairs(2))

        self.assertEqual(5,climbing_stairs(4))
        self.assertEqual(13, climbing_stairs(6))


if __name__ == '__main__':
    unittest.main()