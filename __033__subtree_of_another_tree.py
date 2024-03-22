'''
    572. Subtree of Another Tree
    Given the roots of two binary trees root and subRoot,
    return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
    The tree tree could also be considered as a subtree of itself.

    Constraints:
        The number of nodes in the root tree is in the range [1, 2000].
        The number of nodes in the subRoot tree is in the range [1, 1000].
        -10^4 <= root.val <= 10^4
        -10^4 <= subRoot.val <= 10^4

    #LeetCode: https://leetcode.com/problems/subtree-of-another-tree/description/

    Time Complexity: O( s * t) where s is the number of nodes in the root tree, t is the number of nodes in the subRoot tree
                                in the worst case, for every node in s, all nodes in t are checked, therefore O(s * t)

                                same time complexity for BFS and DFS solutions

    Space Complexity:

                    is_sub_tree_BFS: uses a queue, so O(n) space
                                    same_tree function: O(2^h) - where h is the height of the largest tree between the two
                                    in worst case for every element in the queue, same_tree is called so O(n * 2^h)

                    is_sub_tree_DFS: two recursive calls in each level: O(2^h) h - height of the tree
                                    same_tree function: O(2^h) - where h is the height of the largest tree between the two
                                    so 2 * 2^h = 2 ^ (h + 1), dropping constants still O(2^h)
'''
from collections import deque
from __032__same_binary_tree import same_tree


def is_sub_tree_BFS(root, subRoot):

    queue = deque()

    if root:
        queue.append(root)

    while len(queue) > 0:

        current = queue.popleft()

        #call same_tree function only if values match
        if current.val == subRoot.val:
            #return True only if same_tree returns True, otherwise keep checking other nodes
            if same_tree(current,subRoot):
                return True

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return False

def is_sub_tree_DFS(root, subRoot):
    if not root:
        return False

    #call same_tree function only if values match
    if root.val == subRoot.val:
        #return True only if same_tree returns True, otherwise keep checking other nodes
        if same_tree(root,subRoot):
            return True

    #check the left subtree, right subtree
    #if either them returns true, it satisfies the requirements of a subtree
    return is_sub_tree_DFS(root.left,subRoot) or is_sub_tree_DFS(root.right,subRoot)
