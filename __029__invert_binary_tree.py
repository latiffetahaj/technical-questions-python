'''
    226. Invert Binary Tree
    Given the root of a binary tree, invert the tree, and return its root.

    Constraints:
        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100

    #LeetCode: https://leetcode.com/problems/invert-binary-tree/description/

    Time Complexity: O(n) where n is the number of nodes in the binary tree

    Space Complexity: O(2^h) where h - height of the binary tree
'''

def invert_binary_tree(root):

    if not root:
        return None

    left = root.left
    right = root.right

    #swapping the childs
    root.left = invert_binary_tree(right)
    root.right = invert_binary_tree(left)

    return root


