import unittest
from __000__linked_list_implementation import LinkedList
from __025__has_cycle_linked_list import has_cycle

class TestHasCycle(unittest.TestCase):
        def setUp(self):
            self.linked_list = LinkedList()
            self.linked_list.insert_at_head(2)
            self.linked_list.insert_at_head(3)
            self.linked_list.insert_at_head(4)
            self.linked_list.insert_at_head(10)

        def test_has_cycle(self):
            #before creating a cycle
            head = self.linked_list.getHead()
            self.assertFalse(has_cycle(head))

            #after creating a cycle
            self.linked_list.createCycle(1)
            self.assertTrue(has_cycle(head))


if __name__ == '__main__':
    unittest.main()
