'''
    143. Reorder List
    You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:

    L_0 → L_n → L_1 → L_n-1 → L_2 → L_n-2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    Example:
        Input: head = [1,2,3,4]
        Output: [1,4,2,3]

    Constraints:
        The number of nodes in the list is in the range [1, 5 * 10^4].
        1 <= Node.val <= 1000

    #LeetCode: https://leetcode.com/problems/reorder-list/description/

    Time Complexity: O(n)

    Space Complexity: O(1)
'''

def reorder_list(head):
    #algorithm overview
    #split the list in the middle
    #reverse the second part of the list
    #then merge two lists, at each step taking one node from each list

    #finding the middle of the list

    slow = head
    #initializing one step ahead of slow
    #for odd lists, slow at the end will point exactly in the middle of the list
    #for even lists, slow will point to the first middle node
    #for example for list 1,2,3,4, slow will point at 2
    fast = slow.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #head of the new list will be at slow.next
    new_head = slow.next

    #slow points at the end of first list, set slow.next to be None
    slow.next = None

    #reverse the second list

    prev = None
    current = new_head

    while current:
        temp = current.next
        current.next = prev

        prev = current
        current = temp

    #prev is the head of the reversed list
    new_head = prev

    #merge the lists

    l1 = head
    l2 = new_head

    while l1 and l2:
        temp_1 = l1.next #save the information for next node
        l1.next = l2  #change the link from node of l1 to node of l2
        l1 = temp_1 #move the pointer

        temp_2 = l2.next #save the information for next node
        l2.next = l1 # change the link from node of l2 to node of l1
        l2 = temp_2 #move the pointer



