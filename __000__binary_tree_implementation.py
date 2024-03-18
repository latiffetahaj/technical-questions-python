from collections import deque

class TreeNode:
    def __init__(self, val=0) -> None:
        self.val = val
        self.left = None
        self.right = None


#functions list_to_binary_tree and binary_tree_to_list are built just for testing purposes
#on all the questions that use binary trees
class BinaryTree:

    def __init__(self):
        self.root = None

    #builds the binary tree from a given list as follows
    #it does a level-order build up
    #for example list = [4,2,7,1,3,6,9] yields
    #       4
    #      / \
    #     /   \
    #    /     \
    #   2       7
    #  / \     / \
    # 1   3   6   9
    def list_to_binary_tree(self, list_values):

        if list_values is None or len(list_values) == 0:
            self.root = None
            return

        def build(list_values, index):

            root = TreeNode(list_values[index])

            #left child is located at 2 * (current node index) + 1
            if 2 * index + 1 < len(list_values):
                root.left = build(list_values, 2 * index + 1)
            #right child is located at 2 * (current node index) + 2
            if 2 * index + 2 < len(list_values):
                root.right = build(list_values, 2 * index + 2)

            return root

        self.root = build(list_values, 0)

    # this function uses a breadth-first search algorithm to do a level-order
    # traversal to build the list
    def binary_tree_to_list(self):

        values = []

        def bfs(root):
            #append in the right
            #pop from the left
            queue = deque()

            if root:
                queue.append(root)

            while len(queue) > 0:
                #in-range function generates a sequence of values to go over
                #it uses a loopcount to go over the list of values
                #even if the list changes inside the loop, the number of iterations stays the same
                #so for loop with in-range doesn't detect dynamic changes of the iterations as while-loop does
                for i in range(len(queue)):
                    #pop the first value in the queue
                    current = queue.popleft()
                    values.append(current.val)

                    #append the children of the current node from left to right, if they exist
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)

                #go back up to process the queue if it has the length > 0

        #call the function
        bfs(self.root)

        #return the list
        return values

    def print_preoder(self):
        def preorder(root):
            if not root:
                return

            print(root.val, end=" ")
            preorder(root.left)
            preorder(root.right)

        preorder(self.root)

    def print_inorder(self):
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            print(root.val, end=" ")
            inorder(root.right)

        inorder(self.root)

    def print_postorder(self):
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            print(root.val, end=" ")

        postorder(self.root)


    def get_root(self):
        return self.root