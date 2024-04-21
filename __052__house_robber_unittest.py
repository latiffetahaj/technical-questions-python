import unittest
from __052__house_robber import rob_houses

class TestRobHouses(unittest.TestCase):

    def test_rob_houses(self):
        self.assertEqual(4,rob_houses([1,2,3,1]))

        self.assertEqual(12, rob_houses([2,7,9,3,1]))



if __name__ == '__main__':
    unittest.main()