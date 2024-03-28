'''
    124. Binary Tree Maximum Path Sum
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
    A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
    The path sum of a path is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.

    Constraints:
        The number of nodes in the tree is in the range [1, 3 * 10^4].
        -1000 <= Node.val <= 1000

    #LeetCode: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

    Time Complexity: O(n) where n is the number of nodes in the tree

    Space Complexity: O(2^h) where h - height of the tree
'''
#algorithm is to follow a depth right search
#two main calculations are done
#at each node, the path from left -> root -> right is checked
#we call this path with a split since at root we are spliting on the left and on the right

#before using the left and right result, we check if it's negative and get rid of negative values.
#node passes to its parent the maximum of the two paths
# (node -> left) or (node -> right) so max(left,right) + root.val
def max_path_sum(root):
    max_path = root.val

    def dfs(root):
        if not root:
            return 0
        #dfs on the left and on the right of the tree
        left = dfs(root.left)
        right = dfs(root.right)

        #if returned value is negative, make it zero
        left = max(left,0)
        right = max(right,0)

        nonlocal max_path
        #calculate max_path with a split at the current node
        max_path = max(left + root.val + right, max_path)

        #pass it to parent the max of left or right + root.val
        return max(left,right) + root.val

    dfs(root)
    return max_path

