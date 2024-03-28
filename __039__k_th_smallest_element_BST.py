'''
    230. Kth Smallest Element in a BST
    Given the root of a binary search tree, and an integer k,
    return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

    Constraints:
        The number of nodes in the tree is n.
        1 <= k <= n <= 10^4
        0 <= Node.val <= 10^4

    #LeetCode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

    Time Complexity: O(n)

    Space Complexity: O(n)
'''

#algorithms is as follows
#do an inorder DFS iteratively
#inorder follows: left, root, right
#as soon as one element is popped from the stack, it means that it is processed
#keep track of how many elements are processed and return the value when nr elements processed == k

def kth_smallest_iterative_dfs(root, k):
    stack = []
    elements_processed = 0

    stack.append(root)

    while stack:
        #peek at the stack without popping
        current = stack[-1]

        #first checking if a left child exists, if so push into the stack
        if current.left:
            stack.append(current.left)

            #breaking the link to prevent infinite loop, because at somepoint we will process the root again
            current.left = None
        else:
            current = stack.pop()
            elements_processed += 1


            #k is in interval 1 <= k <= n <= 10^4, so it's guaranteed that
            #a result is returned
            if elements_processed == k:
                return current.val

            if current.right:
                stack.append(current.right)
                current.right = None
