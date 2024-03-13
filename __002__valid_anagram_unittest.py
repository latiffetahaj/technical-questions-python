import unittest
from __002__valid_anagram import isAnagram


class TestIsAnagram(unittest.TestCase):
    def test_true(self):
        self.assertTrue(isAnagram("anagram","nagaram"))
        self.assertTrue(isAnagram("ramush","shumar"))

    def test_false(self):
        self.assertFalse(isAnagram("days", "day"))

    def test_empty(self):
        self.assertTrue(isAnagram("",""))

    def test_null(self):
        self.assertFalse(isAnagram(None,None))






if __name__=='__main__':
	unittest.main()