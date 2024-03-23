'''
    235. Lowest Common Ancestor of a Binary Search Tree
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
    (where we allow a node to be a descendant of itself).”


    Constraints:
        The number of nodes in the tree is in the range [2, 10^5].
        -10^9 <= Node.val <= 10^9
        All Node.val are unique.
        p != q
        p and q will exist in the BST.

    #LeetCode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

    Time Complexity: O(logn) - n => nr of the nodes in the tree

    Space Complexity:
            Recursive Solution:  O(h) - where h is the height of the tree
            Iterative Solution: O(1)
'''
#since all values are unique, for easier testing, both functions return the value of the LCA node of p and q

#recursive solution
def lca_BST_recursive(root, p, q):

    #if both values less than value at the root, search on the left subtree
    if p.val < root.val and q.val < root.val:
        return lca_BST_recursive(root.left,p,q)
    #if both values larger than value at the root, search on the right subtree
    elif p.val > root.val and q.val > root.val:
        return lca_BST_recursive(root.right,p, q)
    #if one of the values is equal to the root, return root as LCA
    else:
        return root.val


#iterative solution
def lca_BST_iterative(root,p,q):
    current = root

    while current:
        if p.val < current.val and q.val < current.val:
            #move pointer to the left subtree
            current = current.left
        elif p.val > current.val and q.val > current.val:
            #move pointer to the right subtree
            current = current.right
        else:
            return current.val