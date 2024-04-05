'''
    5. Sum all nodes from odd levels in the tree.
        With BFS and DFS.

'''
from collections import deque
from __000__binary_tree_implementation import BinaryTree
from drawtree import draw_level_order

'''
    Time Complexity: O(n)
    Space Complexity: O(n) for deque
'''
def sum_odd_levels_BFS(root):
    odd_sum = 0

    queue = deque()
    level = 0

    if root:
        queue.append(root)

    while len(queue) > 0:

        #use for loop to process one level at a time
        #otherwise couldn't detect when to change levels
        for i in range(len(queue)):
            current = queue.popleft()

            #only add to the sum from odd levels
            if level % 2 != 0:
                odd_sum += current.val

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        #each time the for loop exits, one level is processed, so increase level by one
        level += 1

    return odd_sum


def sum_odd_levels_DFS(root):

    def dfs(root, level):
        if not root:
            return 0

    #add the current value only on odd levels
        if level % 2 != 0:
            return root.val + dfs(root.left, level + 1) + dfs(root.right, level + 1)
        else:
            return 0 + dfs(root.left, level + 1) + dfs(root.right, level + 1)

    return dfs(root,0)


def main():
    tree_1 = BinaryTree()

    tree_1.list_to_binary_tree([1,2,5,12,22,0,0,1,2])
    root = tree_1.get_root()

    draw_level_order('{1,2,5,12,22,0,0,1,2}')

    print('BFS sum',sum_odd_levels_BFS(root))

    print('DFS sum', sum_odd_levels_DFS(root))


if __name__ == '__main__':
    main()