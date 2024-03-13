import unittest
from __014__most_water_container import most_water_container

class TestMostWaterContainer(unittest.TestCase):
    def test(self):
        self.assertEqual(49, most_water_container([1,8,6,2,5,4,8,3,7]))
        self.assertEqual(1,most_water_container([1,1]))
        self.assertEqual(0,most_water_container([0,1]))


if __name__ == '__main__':
    unittest.main()


