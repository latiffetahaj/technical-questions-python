import unittest
from __084__non_overlapping_intervals import erase_overlapping_intervals

class TestEraseOverlappingIntervals(unittest.TestCase):
    def test_overlapping_intervals(self):
        self.assertEqual(1, erase_overlapping_intervals([[1,2],[2,3],[3,4],[1,3]]))
        self.assertEqual(0, erase_overlapping_intervals([[1,2]]))
        self.assertEqual(3, erase_overlapping_intervals([[1,3], [1,3], [1,3], [1,3]]))


if __name__ == '__main__':
    unittest.main()