import unittest
from __093__max_area_island import max_area

class TestMaxArea(unittest.TestCase):
    def test_max_area(self):
        grid_1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        self.assertEqual(6, max_area(grid_1))

        grid_2 = [[0,0,0,0,0,0,0,0]]
        self.assertEqual(0, max_area(grid_2))


if __name__ == '__main__':
    unittest.main()