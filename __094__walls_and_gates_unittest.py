import unittest
from __094__walls_and_gates import walls_and_gates

class TestWallsAndGates(unittest.TestCase):
    def test_walls_and_gates(self):
        grid_1 = [[2147483647,-1,0,2147483647],
                [2147483647,2147483647,2147483647,-1],
                [2147483647,-1,2147483647,-1],
                [0,-1,2147483647,2147483647]]

        output_grid_1 = [[3,-1,0,1],
                        [2,2,1,-1],
                        [1,-1,2,-1],
                        [0,-1,3,4]]

        walls_and_gates(grid_1)
        self.assertEqual(output_grid_1, grid_1)

        grid_2 = [[0,-1],
                [2147483647,2147483647]]

        output_grid_2 = [[0,-1],
                        [1,2]]

        walls_and_gates(grid_2)
        self.assertEqual(output_grid_2, grid_2)
if __name__ == '__main__':
    unittest.main()