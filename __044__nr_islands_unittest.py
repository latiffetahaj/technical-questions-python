import unittest
from __044__nr_islands import nr_islands

class TestNrIslands(unittest.TestCase):
    def test_nr_islands(self):
        grid_1 = [  ["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]]


        grid_2 = [  ["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]]


        self.assertEqual(1, nr_islands(grid_1))
        self.assertEqual(3,nr_islands(grid_2))


if __name__ == '__main__':
    unittest.main()


