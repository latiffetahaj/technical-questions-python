'''
    199. Binary Tree Right Side View
    Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

    Constraints:
        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100

    #LeetCode: https://leetcode.com/problems/binary-tree-right-side-view/description/

    Time Complexity: O(n) where n is the number of nodes in the tree

    Space Complexity: O(n) for using the queue
'''
from collections import deque

#algorithm
#do a BFS level order traversal from right to left
#append to the final result only the first value of each level
#since we're traversing from right to left, in each level, the first value is going to be the right side view
def binary_tree_right_side_view(root):
    q = deque()
    result = []

    if root:
        q.append(root)

    while q:

        index = 1
        for i in range(len(q)):
            current = q.popleft()

            #append only the first value in each level
            if index == 1:
                result.append(current.val)
                index += 1

            if current.right:
                q.append(current.right)

            if current.left:
                q.append(current.left)

    return result

