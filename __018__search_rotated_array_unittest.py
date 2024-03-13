import unittest
from __18__search_rotated_array import search_rotated_array

class TestSearchRotatedArray(unittest.TestCase):
    def test_target_found(self):
        self.assertEqual(4, search_rotated_array([4,5,6,7,0,1,2],0))
        self.assertEqual(6,search_rotated_array([3,4,5,6,7,-2,-1], -1))

    def test_target_not_found(self):
        self.assertEqual(-1,search_rotated_array([1,2,3,4,5,6,7,8], 123))
        self.assertEqual(-1,search_rotated_array([12,13,14,0,5,8], -4))




if __name__ == '__main__':
    unittest.main()


