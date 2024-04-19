import unittest
from __049__word_search import has_word

class TestSearchWord(unittest.TestCase):

    def test_search_word(self):

        board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]]
        word = "SEE"

        self.assertTrue(has_word(board,word))


        board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]]
        word = "ABCB"

        self.assertFalse(has_word(board,word))


if __name__ == '__main__':
    unittest.main()