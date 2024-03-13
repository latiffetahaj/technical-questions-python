'''
    23. Merge k Sorted Lists
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.


    Input is a list with heads of each list that is going to be merged
    Example:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
        [
        1->4->5,
        1->3->4,
        2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6

    Constraints:
        k == lists.length
        0 <= k <= 10^4
        0 <= lists[i].length <= 500
        -10^4 <= lists[i][j] <= 10^4
        lists[i] is sorted in ascending order.
        The sum of lists[i].length will not exceed 10^4.

    #LeetCode: https://leetcode.com/problems/merge-k-sorted-lists/description/

    Time Complexity: O(n logk), where n = lists[i].length, and k = lists.length

    Space Complexity: O(1)
'''

from __024__merge_2_sorted_lists import merge_two_lists

def merge_k_sorted_lists(lists):
    #the algorithm is as follows:
    #merge two lists at a time using the merge_2_sorted_list function
    #at the end, the output contains one head of the merged list

    if lists is None or len(lists) == 0:
        return None

    while len(lists) > 1:
        merged_lists = []

        #step is 2 because in each iteration, 2 lists are merged
        for i in range(0, len(lists), 2):
            l1 = lists[i]

            #for odd length lists, check if i is inbound or make l2 = None
            l2 = lists[i + 1] if (i+1) < len(lists) else None
            l1_l2 = merge_two_lists(l1,l2)

            #append the result
            merged_lists.append(l1_l2)

        #example, input = [l1,l2,l3,l4]
        #after first iteration it becomes [l_12, l_34]
        #now the new input is this one so update it
        lists = merged_lists

    #at the end lists will contain only one element, the head of the merged list
    return lists[0]





