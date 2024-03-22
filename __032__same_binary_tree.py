'''
    100. Same Tree
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    Constraints:
        The number of nodes in both trees is in the range [0, 100].
        -10^4 <= Node.val <= 10^4

    #LeetCode: https://leetcode.com/problems/same-tree/description/

    Time Complexity: O(p + q) - p - nr of nodes in first tree,
                                q - nr of nodes in the second tree.

    Space Complexity: O(2^h) - where h is the height of the largest tree between the two
'''

def same_tree(p, q):

    if p and q:
        #only if the values don't match, return False
        if p.val != q.val:
            return False
    elif not p and not q:
        #if both not None
        return True
    else:
        #if one of them is None
        return False

    return same_tree(p.left,q.left) and same_tree(p.right,q.right)

