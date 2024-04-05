

'''
Assume each node has a link to its parent.
2. Given two nodes, find the lowest common ancestor of the two nodes.
        One solution with constant space
        One solution with non-constant space, faster time

Is it a binary search tree??
Are node values unique?
Can a node be an ancestor of itself?
Are given nodes guaranteed to be in the tree?

for BST solution is at __035__ file with unique node values
'''
from __000__binary_tree_implementation import TreeNode, BinaryTree
import drawtree


'''
if the binary tree is not a binary search tree
assuming the given nodes are in the tree
and assuming that values are unique

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(2^h) where h is the height of the tree
'''
def lowest_common_ancestor(root,p,q):
    #create a treeNode to store the result
    result = TreeNode()

    def dfs(root):
        if not root:
            return False

        left = dfs(root.left)
        right = dfs(root.right)

        nonlocal result
        #if both right and left subtrees return true
        #that means along the way both p and q are found
        #so return this node
        if left and right:
            result = root

        #return true if any of the values matches the root
        #of if left or right is true, because this means we encountered one of the values earlier
        if root.val == p.val or root.val == q.val or left or right:
            return True
        else:
            return False


    dfs(root)

    return result


def main():
    tree = BinaryTree()

    tree.list_to_binary_tree([1,12,3,-5,-6,-20,20])

    drawtree.draw_level_order('{1,12,3,-5,-6,-20,20}')

    root = tree.get_root()
    p = TreeNode(-6)
    q = TreeNode(20)
    result = lowest_common_ancestor(root,p,q)

    print(result.val)


if __name__ == '__main__':
    main()

