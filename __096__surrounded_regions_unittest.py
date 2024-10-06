import unittest
from __096__surrounded_regions import mark_surrounded_regions

class TestSurrounedRegions(unittest.TestCase):
    def test_surrounded_regions(self):
        board_1 = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]]


        output_1 = [["X","X","X","X"],
                ["X","X","X","X"],
                ["X","X","X","X"],
                ["X","O","X","X"]]


        mark_surrounded_regions(board_1)
        self.assertEqual(output_1, board_1)

        board_2 = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","X","X"],
                ["X","O","O","O"]]

        output_2 = [["X","X","X","X"],
                ["X","X","X","X"],
                ["X","X","X","X"],
                ["X","O","O","O"]]

        mark_surrounded_regions(board_2)
        self.assertEqual(output_2, board_2)

if __name__ == '__main__':
    unittest.main()