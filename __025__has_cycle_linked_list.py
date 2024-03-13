'''
    141. Linked List Cycle
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
    Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.

    Constraints:
        The number of the nodes in the list is in the range [0, 10^4].
        -10^5 <= Node.val <= 10^5
        pos is -1 or a valid index in the linked-list.

    #LeetCode: https://leetcode.com/problems/linked-list-cycle/description/

    Time Complexity: O(n)

    Space Complexity: O(1)
'''

def has_cycle(head):
    slow = head
    fast = head

    #checking if fast.next exists, that means list needs to have at least two nodes to detect for a cycle
    #a list with only one node can't have a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
