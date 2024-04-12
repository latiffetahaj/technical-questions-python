import unittest
from __045__subsets import subsets


class TestSubsets(unittest.TestCase):

    def test_subsets(self):
        self.assertEqual([[]],subsets([]))

        self.assertEqual([[1],[]],subsets([1]))

        self.assertEqual([[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []],subsets([1,2,3]))



if __name__ == '__main__':
    unittest.main()