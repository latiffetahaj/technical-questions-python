import unittest
from __095__rotting_oranges import oranges_rotting

class TestOragnesRotting(unittest.TestCase):
    def test_oranges_rotting(self):

        grid_1 = [[2,1,1],
                [1,1,0],
                [0,1,1]]
        self.assertEqual(4, oranges_rotting(grid_1))


        grid_2 = [[2,1,1],
                [0,1,1],
                [1,0,1]]
        self.assertEqual(-1, oranges_rotting(grid_2))


        grid_3 = [[0,2]]
        self.assertEqual(0, oranges_rotting(grid_3))

if __name__ == '__main__':
    unittest.main()