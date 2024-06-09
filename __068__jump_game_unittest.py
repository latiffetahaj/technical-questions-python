import unittest
from __068__jump_game import can_jump

class TestJumpGame(unittest.TestCase):
    def test_can_jump(self):
        self.assertTrue(can_jump([2,3,1,1,4]))
        self.assertFalse(can_jump([3,2,1,0,4]))
        self.assertTrue(can_jump([1]))
        self.assertFalse(can_jump([0,1]))


if __name__ == '__main__':
    unittest.main()