import unittest
from __073__min_window_substring import min_window

class TestMinWindow(unittest.TestCase):
    def test_min_window(self):
        self.assertEqual('BANC', min_window('ADOBECODEBANC', 'ABC'))
        self.assertEqual('', min_window('aaaaa', 'bba'))

        self.assertEqual('ldhel', min_window('helloworldhello', 'lld'))

if __name__ == '__main__':
    unittest.main()