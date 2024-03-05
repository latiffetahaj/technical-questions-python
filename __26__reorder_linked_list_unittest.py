import unittest
from __00__linked_list_implementation import LinkedList
from __26__reorder_linked_list import reorder_list

class TestReorderList(unittest.TestCase):

        def setUp(self):
            self.linked_list = LinkedList()
            self.linked_list.insert_at_tail(1)
            self.linked_list.insert_at_tail(2)
            self.linked_list.insert_at_tail(3)
            self.linked_list.insert_at_tail(4)


        def test_reorder_list(self):

            #before list reorder
            self.assertEqual([1,2,3,4],self.linked_list.getValues())

            head = self.linked_list.getHead()
            reorder_list(head)

            #after list reorder
            self.assertEqual([1,4,2,3],self.linked_list.getValues())

if __name__ == '__main__':
    unittest.main()