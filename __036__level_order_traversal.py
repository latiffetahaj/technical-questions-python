"""
    102. Binary Tree Level Order Traversal
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).

    Constraints:
        The number of nodes in the tree is in the range [0, 2000].
        -1000 <= Node.val <= 1000

    #LeetCode: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

    Time Complexity: O(n) - n => nr of the nodes in the tree

    Space Complexity: O(n) - n => nr of the nodes in the tree
"""

from collections import deque


# algorithm:
# do Breadth-First-Search (BFS) on the tree
# use a for loop to process the nodes one level at a time
def level_order_traversal(root):
    result = []

    q = deque()

    if root:
        q.append(root)

    while q:
        # a list to keep the values for the current level of processing
        current_level = []

        for i in range(len(q)):
            current = q.popleft()

            current_level.append(current.val)

            # add children of the current node from left to right if they exist
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

        # after processing one level, append to the final result as a sublist
        result.append(current_level)

    return result
