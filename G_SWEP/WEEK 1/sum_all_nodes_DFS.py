'''
    4.Sum a tree with DFS in under 3 minutes.
'''
from __000__binary_tree_implementation import BinaryTree

#recursive solution
def dfs_sum_all_nodes(root):
    if not root:
        return 0

    #preorder traversal
    #visit
    #left
    #right
    return root.val + dfs_sum_all_nodes(root.left) + dfs_sum_all_nodes(root.right)

    #inorder would be
    #left
    #visit
    #right
    #return dfs_sum_all_nodes(root.left) + root.val + dfs_sum_all_nodes(root.right)

    #postorder
    #left
    #right
    #visit
    #return dfs_sum_all_nodes(root.left) + dfs_sum_all_nodes(root.right) + root.val


def dfs_sum_all_nodes_iterative(root):
    stack = []

    total_sum = 0
    if root:
        stack.append(root)

    while stack:
        current = stack.pop()

        total_sum += current.val

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    return total_sum

def inorder_traversal(root):
    result = []
    def dfs(root):
        if not root:
            return

        dfs(root.left)
        result.append(root.val)
        dfs(root.right)

    dfs(root)
    return result


def main():
        tree_1 = BinaryTree()

        tree_1.list_to_binary_tree([10,8,20,6,9,12,22])

                #      10
                #      / \
                #     /   \
                #    /     \
                #   8      20
                #  / \     / \
                # 6   9   /   \
                #        12   22

        root = tree_1.get_root()

        print(inorder_traversal(root))

if __name__ == '__main__':
    main()
