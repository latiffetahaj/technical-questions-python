"""
    105. Construct Binary Tree from Preorder and Inorder Traversal
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
    inorder is the inorder traversal of the same tree, construct and return the binary tree.

    Constraints:
        1 <= preorder.length <= 3000
        inorder.length == preorder.length
        -3000 <= preorder[i], inorder[i] <= 3000
        preorder and inorder consist of unique values.
        Each value of inorder also appears in preorder.
        preorder is guaranteed to be the preorder traversal of the tree.
        inorder is guaranteed to be the inorder traversal of the tree.

    #LeetCode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

    Time Complexity:
    Space Complexity:
"""
from __000__binary_tree_implementation import TreeNode

#preorder traversal => root, left, right
#inorder traversal => left, root, right

#algorithm is as follows:
#from the preorder array, preorder[0] is the root due to preorder traversal
#now in the inorder traversal, we search in which index is this root = preorder[0] located

#since inorder follows the order left, root, right,
#this tells that all values [0,root) belong to left-subtree
#all values (root,len(inorder) -1] belong to right-subtree
#inorder = [left, root, right]
#in the left-side recursive call, left-portion of inorder is passed
#in the right-side recursive call, right-portion of inorder is passed

#now the length of left, and right portions in inorder determine how many values are in the left and right subtrees respectively
# from preorder = [root, left, right],
# in the left-side recursive call, we pass as preorder same number of values as left side of inorder
# in the right-sdie recursive call, we pass as preorder same number of values as right side of inorder

def construct_tree(preorder,inorder):

    if not preorder or not inorder:
        return None

    #root is the first value in preorder
    root = TreeNode(preorder[0])

    #find the index where root is located in inorder array
    mid = inorder.index(preorder[0])

    #use this mid index to divide preorder and inorder arrays
    root.left = construct_tree(preorder[1:mid+1], inorder[:mid])
    root.right = construct_tree(preorder[mid+1:], inorder[mid+1:])

    return root

#for testing purposes
def values_preorder(root):
    values = []
    def preorder(root):
        if not root:
            return
        values.append(root.val)
        preorder(root.left)
        preorder(root.right)

    preorder(root)

    return values
