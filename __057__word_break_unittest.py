import unittest
from __057__word_break import word_break

class TestWordBreak(unittest.TestCase):

    def test_word_break(self):
        self.assertTrue(word_break('leetcode', ['code', 'leet']))
        self.assertFalse(word_break('catsandog', ['cats','dog','sand','and','cat']))


if __name__ == '__main__':
    unittest.main()