'''
    104. Maximum Depth of Binary Tree
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Constraints:
        The number of nodes in the tree is in the range [0, 10^4].
        -100 <= Node.val <= 100

    #LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

    Time Complexity: O(n) where n is the number of nodes in the binary tree

    Space Complexity: O(2^h) where h - height of the binary tree, in this case depth of the tree
'''

from collections import deque

#recursive solution using Depth First Search - DFS
def max_depth(root):

    #the depth of a null node is zero
    if not root:
        return 0

    #if root is not null, max depth is calculated as follows
    #get the max of depth from the left subtree and depth of the right subtree
    #then add 1 at the root, because when root is processed, depth increases by 1
    return 1 + max(max_depth(root.left), max_depth(root.right))


#iterative solution using Breadth First Search - BFS
#this is a level order traversal, so we keep a depth variable
#in each level, depth variable is incremented
def max_depth_BFS(root):

    depth = 0
    queue = deque()

    if root:
        queue.append(root)

    while len(queue) > 0:

        for i in range(len(queue)):
            #process the current node
            current = queue.popleft()

            #add its childs to the queue, if they exist
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        #each time the for loop exits, one level is processed, so increase depth by one
        depth += 1

    return depth






