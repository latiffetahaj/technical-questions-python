import unittest
from __069__jump_game_II import min_jump

class TestMinJump(unittest.TestCase):
    def test_min_jump(self):
        self.assertEqual(2, min_jump([2,3,1,1,4]))
        self.assertEqual(2, min_jump([2,3,0,1,4]))

        self.assertEqual(1, min_jump([1,1]))


if __name__ == '__main__':
    unittest.main()