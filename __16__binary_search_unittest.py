import unittest
from __16__binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_target_found(self):
        self.assertEqual(4, binary_search([-1,0,3,5,9,12],9))
        self.assertEqual(5,binary_search([10,13,15,200,230,500,600],500))

    def test_target_not_found(self):
        self.assertEqual(-1, binary_search([0,1,2,3,4,5,6,7], 12))
        self.assertEqual(-1, binary_search([-4,-2,0,5,7,9,10,15,44,55], 8))


if __name__ == '__main__':
    unittest.main()