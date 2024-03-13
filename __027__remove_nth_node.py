'''
    19. Remove Nth Node From End of List
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Example:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]

    Constraints:
        The number of nodes in the list is sz.
        1 <= sz <= 30
        0 <= Node.val <= 100
        1 <= n <= sz

    #LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
    Time Complexity: O(n)

    Space Complexity: O(1)
'''

def remove_nth_node(head,n):

    #distance between two pointers, initially is zero because they both point at head
    distance = 0

    left = head
    right = head

    #need to move the right pointer until the distance is n+1
    # reason for n+1: the left pointer needs to stop one node before the one that we need to remove

    while right and distance != (n+1):
        right = right.next
        distance += 1

    #checking the distance
    #if it's not n+1, that means the node to remove is head, so just return left.next
    #this happens when n = length of list
    if distance != (n+1):
        return left.next

    #move two pointers until the end by one step each time
    while right:
        left = left.next
        right = right.next

    #delete
    left.next = left.next.next

    return head
