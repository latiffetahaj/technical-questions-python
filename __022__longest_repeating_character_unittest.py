import unittest
from __022__longest_repeating_character import character_replacement

class TestLongestRepeatingCharacter(unittest.TestCase):
    def test_one_character(self):
        self.assertEqual(1, character_replacement('A', 1))
        self.assertEqual(4, character_replacement("AABABBA",1))

    def test_multiple_characters(self):
        self.assertEqual(4, character_replacement("ABAB",2))
        self.assertEqual(5,character_replacement("CDCDC",2))




if __name__ == '__main__':
    unittest.main()