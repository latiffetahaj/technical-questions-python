import unittest
from __000__linked_list_implementation import LinkedList
from __028__merge_k_sorted_lists import merge_k_sorted_lists

class TestMergeKSortedLists(unittest.TestCase):
    def setUp(self):
        self.list1 = LinkedList()
        self.list2 = LinkedList()
        self.list3 = LinkedList()

        self.list1.insert_at_head(3)
        self.list1.insert_at_head(2)
        self.list1.insert_at_head(1)

        self.list2.insert_at_head(4)
        self.list2.insert_at_head(3)
        self.list2.insert_at_head(1)

        self.list3.insert_at_head(6)
        self.list3.insert_at_head(5)
        self.list3.insert_at_head(4)
        self.list3.insert_at_head(2)

    def test_merge_k_lists(self):
        head1 = self.list1.getHead()
        head2 = self.list2.getHead()
        head3 = self.list3.getHead()

        merged_head = merge_k_sorted_lists([head1,head2,head3])

        self.assertEqual([1,1,2,2,3,3,4,4,5,6],self.list1.getValuesFromHead(merged_head))


if __name__ == '__main__':
    unittest.main()