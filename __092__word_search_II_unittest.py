import unittest
from __092__word_search_II import find_words

class TestFindWords(unittest.TestCase):
    def test_find_words(self):
        self.assertEqual(["oath","eat"], find_words(["oath","pea","eat","rain"], [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]] ))

        self.assertEqual([], find_words(["abcb"], [["a","b"],["c","d"]]))
if __name__ == '__main__':
    unittest.main()