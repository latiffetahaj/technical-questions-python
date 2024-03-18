'''
    543. Diameter of Binary Tree
    Given the root of a binary tree, return the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root.
    The length of a path between two nodes is represented by the number of edges between them.

    Constraints:
        The number of nodes in the tree is in the range [0, 10^4].
        -100 <= Node.val <= 100

    #LeetCode: https://leetcode.com/problems/diameter-of-binary-tree/description/

    Time Complexity: O(n) where n is the number of nodes in the binary tree

    Space Complexity: O(2^h) where h - height of the binary tree, in this case depth of the tree
'''

def diameter_binary_tree(root):

    diameter = 0

    #dfs calculates the height using depth first search
    #then in each height calculation it updates the diameter if needed
    #algorithm is as follows
    # a None root has a height of -1
    #at a current node, height is calculated as the max(left subtree, right subtree) + 1
    #so in the current node, we keep track of largest height of its children + add 1 to account for the current node

    #diameter is calculated as left height + right height + 2
    # 2 is added because of these two edges
    # 1. current-node -(to) left child
    # 2. current-node -(to) right child
    def dfs(root):
        if not root:
            return - 1

        left = dfs(root.left)
        right = dfs(root.right)

        #nonlocal keyword to tell python to look for definition in the outer scope
        nonlocal diameter

        #update the diamater
        diameter = max(diameter, left + right + 2)

        #return the height
        return 1 + max(left,right)


    #call the function
    dfs(root)

    return diameter