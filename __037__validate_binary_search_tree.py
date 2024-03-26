"""
    98. Validate Binary Search Tree
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

    Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        -2^31 <= Node.val <= 2^31 - 1

    #LeetCode: https://leetcode.com/problems/validate-binary-search-tree/description/

    Time Complexity: O(n) n => nr of nodes in the tree
    Space Complexity: 2^h where h is the height of the tree
"""
#to determine if a given BST is valid, the approach is by updating the range of possible values that the given node can have
#for example initially, root can be any value from -inf to +inf theoretically, so (-inf < root.val < +inf)
#now the left subtree can contain only the values in range (-inf < root.val)
#the right subtree can contain only the values in range (root.val < +inf)

#so when calling the left-subtree, the right-bound is updated
#when calling the right-subtree, the left-bound is updated

def is_valid_BST(root):

    def valid(root, left_bound, right_bound):
        if not root:
            return True

        #if root.val NOT within range:
        if not (root.val > left_bound and root.val < right_bound):
            return False

        #both left and right subtrees need to return true, for the entire tree to be valid BST
        #update the right-bound on the left-subtree
        return (valid(root.left, left_bound,root.val) and
                #update the left-bound on the right-subtree
                valid(root.right, root.val, right_bound))

    #call the function with inital range (-inf,+inf) for the root
    return valid(root, float('-inf'), float('+inf'))

