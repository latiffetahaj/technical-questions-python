import unittest
from __042_implement_trie_prefix import Trie

class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

        self.trie.insert('Hello')
        self.trie.insert('world')


    def test_search(self):
        self.assertTrue(self.trie.search('world'))

    def test_startsWith(self):
        self.assertTrue(self.trie.startsWith('wo'))


if __name__ == '__main__':
    unittest.main()