'''
    110. Balanced Binary Tree
    Given a binary tree, determine if it is height-balanced.
    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


    Constraints:
        The number of nodes in the tree is in the range [0, 5000].
        -10^4 <= Node.val <= 10^4

    #LeetCode: https://leetcode.com/problems/balanced-binary-tree/description/

    Time Complexity: O(n) - n => nr of the nodes in the tree

    Space Complexity: O(2^h) - where h is the height of the tree
'''

def is_balanced(root):

    #this function uses the DFS algorithm,
    #it returns two values, boolean which states is the tree balanced at that step
    #and also the max height
    def dfs(root):

        if not root:
            return [True,0]

        #before evaluating the root, check the left and right subtrees
        left = dfs(root.left)
        right = dfs(root.right)

        #current node is balanced iif left and right subtrees are balanced and iff
        #difference of heights is <= 1
        #two returned values, index[0] accesses the boolean, index[1] accesses the height
        balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]


    #call the function, get only the first value, the boolean
    return dfs(root)[0]