import unittest

from __00__linked_list_implementation import LinkedList
from __24__merge_2_sorted_lists import merge_two_lists

class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.list1 = LinkedList()
        self.list2 = LinkedList()

        self.list1.insert_at_head(3)
        self.list1.insert_at_head(2)
        self.list1.insert_at_head(1)

        self.list2.insert_at_head(4)
        self.list2.insert_at_head(3)
        self.list2.insert_at_head(1)


    def test_merge_lists(self):
        #list1 = [1,2,3]
        head_1 = self.list1.getHead()

        #list2 = [1,3,4]
        head_2 = self.list2.getHead()

        #merge two lists
        head_merged = merge_two_lists(head_1,head_2)

        self.assertEqual([1,1,2,3,3,4], self.list1.getValuesFromHead(head_merged))



if __name__ == '__main__':
    unittest.main()


