'''
    206. Reverse Linked List
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Constraints:
        The number of nodes in the list is the range [0, 5000].
        -5000 <= Node.val <= 5000

    #LeetCode: https://leetcode.com/problems/reverse-linked-list/description/

    Iterative Solution:
        Time Complexity: O(n)
        Space Complexity: O(1)

    Recursive Solution:
        Time Complexity: O(n)
        Space Complexity: O(n) because of recursive calls
'''

#Iterative Solution
def reverse_list(head):
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev

        prev = current
        current = temp

    return prev

#Recursive Solution
def reverse_list_recursive(head):
    if not head:
        return None

    new_head = head
    if head.next:
        new_head = reverse_list_recursive(head.next)
        head.next.next = head

    head.next = None

    return new_head
