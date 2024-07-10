import unittest
from __083__merge_intervals import merge_intervals

class TestMergeIntervals(unittest.TestCase):

    def test_merge_intervals(self):
        self.assertEqual([[1,6],[8,10],[15,18]], merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
        self.assertEqual([[1,5]], merge_intervals([[1,4],[4,5]]))


if __name__ == '__main__':
    unittest.main()