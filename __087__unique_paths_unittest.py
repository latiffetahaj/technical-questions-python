import unittest
from __087__unique_paths import unique_paths

class TestUniquePaths(unittest.TestCase):

    def test_unique_paths(self):
        self.assertEqual(28, unique_paths(3, 7))
        self.assertEqual(3, unique_paths(3,2))
        self.assertEqual(1, unique_paths(1,1))


if __name__ == '__main__':
    unittest.main()