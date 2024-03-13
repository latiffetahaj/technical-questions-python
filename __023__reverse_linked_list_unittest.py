import unittest
from __23__reverse_linked_list import reverse_list
from __00__linked_list_implementation import LinkedList

class TestReverseList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.insert_at_head(2)
        self.linked_list.insert_at_head(3)
        self.linked_list.insert_at_head(4)


    def test_reverse(self):
        #list before reversing
        self.assertEqual([4,3,2], self.linked_list.getValues())

        head = self.linked_list.getHead()
        head_of_reversed = reverse_list(head)

        #list after reversing
        self.assertEqual([2,3,4],self.linked_list.getValuesFromHead(head_of_reversed))


if __name__ == '__main__':
    unittest.main()

