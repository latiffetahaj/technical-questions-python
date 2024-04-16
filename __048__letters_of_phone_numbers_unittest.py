import unittest
from __048__letters_of_phone_numbers import letter_combinations

class TestLetterCombinatons(unittest.TestCase):
    def test_letter_combinations(self):

        self.assertEqual(['ad','ae','af','bd','be','bf','cd','ce','cf'], letter_combinations('23'))

        self.assertEqual(['w','x','y','z'],letter_combinations('9'))





if __name__ == '__main__':
    unittest.main()