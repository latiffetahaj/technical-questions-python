import unittest
from __064__kth_largest_element_in_array import find_kth_largest

class TestKthLargest(unittest.TestCase):
    def test_kth_largest(self):
        self.assertEqual(4, find_kth_largest([7,2,3,4,1,0], 2))
        self.assertEqual(7, find_kth_largest([7,2,3,4,1,0], 1))
        self.assertEqual(0, find_kth_largest([0], 1))



if __name__ == '__main__':
    unittest.main()