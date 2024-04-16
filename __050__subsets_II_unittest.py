import unittest
from __050__subsets_II import subsets_II


class TestSubsetsII(unittest.TestCase):
    def test_subsets_II(self):
        self.assertEqual([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], subsets_II([2,1,2]))

        self.assertEqual([[], [0]], subsets_II([0]))

if __name__ == '__main__':
    unittest.main()