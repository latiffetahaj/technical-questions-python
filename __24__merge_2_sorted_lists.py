'''
    21. Merge Two Sorted Lists
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.

    Constraints:
        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both list1 and list2 are sorted in non-decreasing order.

    #LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/description/

    Time Complexity: O(n)

    Space Complexity: O(1)
'''
from __00__linked_list_implementation import ListNode

def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next


    if list1:
        # when list1 is longer than list2, just attach the remaining of list1 at the end
        tail.next = list1
    elif list2:
        #when list2 is longer than list1, just attach the remaining of list2 at the end
        tail.next = list2

    #dummy.next is the head of the merged list
    return dummy.next
