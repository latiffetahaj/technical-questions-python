import unittest
from __17__min_rotated_array import find_min


class TestFindMin(unittest.TestCase):
    def test(self):
        self.assertEqual(0,find_min([4,5,6,7,0,1,2,3]))
        self.assertEqual(-5, find_min([1,2,3,-5,-1,0]))
        self.assertEqual(1,find_min([4,5,6,1,2,3]))



if __name__ == '__main__':
    unittest.main()