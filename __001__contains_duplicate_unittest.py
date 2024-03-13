import unittest

from __001__contains_duplicate import contains_duplicate


class TestContainsDuplicate(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(contains_duplicate([1,1,1,2]))
        self.assertTrue(contains_duplicate([1,2,3,7,7]))

    def test_empty(self):
        self.assertFalse(contains_duplicate([]))

    def test_null(self):
        self.assertFalse(contains_duplicate(None))

    def test_false_cases(self):
        self.assertFalse(contains_duplicate([8]))
        self.assertFalse(contains_duplicate([1,2,3,4]))


if __name__=='__main__':
	unittest.main()