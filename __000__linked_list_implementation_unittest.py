import unittest
from __000__linked_list_implementation import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.insert_at_head(2)
        self.linked_list.insert_at_head(3)
        self.linked_list.insert_at_head(4)


    def test_get_values(self):
        self.assertEqual([4,3,2],self.linked_list.getValues())

    def test_remove(self):
        #remove at head
        self.linked_list.remove(0)
        self.assertEqual([3,2],self.linked_list.getValues())

        #add back the same value
        self.linked_list.insert_at_head(4)

        #remove at tail
        self.linked_list.remove(2)
        self.assertEqual([4,3],self.linked_list.getValues())

        #add back the same value
        self.linked_list.insert_at_tail(2)

        #remove in the middle
        self.linked_list.remove(1)
        self.assertEqual([4,2],self.linked_list.getValues())


if __name__ == '__main__':
        unittest.main()