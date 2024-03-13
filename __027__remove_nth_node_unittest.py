import unittest
from __00__linked_list_implementation import LinkedList
from __27__remove_nth_node import remove_nth_node

class TestRemoveNthNode(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.insert_at_tail(1)
        self.linked_list.insert_at_tail(2)
        self.linked_list.insert_at_tail(3)
        self.linked_list.insert_at_tail(4)

    def test_remove_nth_node_last(self):
        #remove the nth node where n == length of list
        head = self.linked_list.getHead()

        #remove last node from end
        new_head = remove_nth_node(head,4)
        self.assertEqual([2,3,4],self.linked_list.getValuesFromHead(new_head))

    def test_remove_nth_node_first(self):
        #remove first node from end
        head = self.linked_list.getHead()
        new_head = remove_nth_node(head,1)

        self.assertEqual([1,2,3],self.linked_list.getValuesFromHead(new_head))

    def test_remove_nth_node_middle(self):

        head = self.linked_list.getHead()

        #remove third node from end
        new_head = remove_nth_node(head,3)

        self.assertEqual([1,3,4], self.linked_list.getValuesFromHead(new_head))

if __name__ == '__main__':
    unittest.main()