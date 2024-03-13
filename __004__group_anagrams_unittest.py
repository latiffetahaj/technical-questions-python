import unittest

from __004__group_anagrams import groupAnagrams

class TestGroupAnagrams(unittest.TestCase):
    def test(self):
        self.assertEqual([['eat', 'tea','ate'], ['tan', 'nat'], ['bat']], groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        self.assertEqual([["a"]],groupAnagrams(["a"]))


    def test_empty(self):
        self.assertEqual([[""]], groupAnagrams([""]))

    def test_null(self):
        self.assertEqual(None,groupAnagrams(None))




if __name__ == '__main__':
    unittest.main()