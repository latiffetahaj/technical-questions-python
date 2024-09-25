import unittest
from __091__add_search_words_ds import WordDictionary

class TestWordDictionary(unittest.TestCase):

    def setUp(self):
        self.wordDictionary = WordDictionary()
        self.wordDictionary.addWord("bad")
        self.wordDictionary.addWord("dad")
        self.wordDictionary.addWord("mad")


    def test_search(self):
        self.assertTrue(self.wordDictionary.search("bad"))
        self.assertTrue(self.wordDictionary.search(".ad"))

        self.assertFalse(self.wordDictionary.search('.md'))


if __name__ == '__main__':
    unittest.main()