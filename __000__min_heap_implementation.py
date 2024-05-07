'''
    Design a Minimum Heap (aka a Priority Queue) class.

    Your MinHeap class should support the following operations:

        MinHeap() will initialize an empty minimum heap.
        void push(int val) will add val to the heap.
        int pop() will remove and return the smallest element in the heap. If the heap is empty, return -1.
        int top() will return the smallest element in the heap without removing it. If the heap is empty, return -1.
        void heapify(int[] nums) will build a minimum heap from nums.


    Note: push and pop should be implemented in O(logn) time complexity,
    while top should be implemented in O(1),
    and heapify should be implemented in O(n) time complexity.

'''
# The provided solution uses one-based indexing as follows:
# The value at index 0 is a dummy value.
# The rest uses these formulas:
# left_child of i = 2 * i
# right_child of i = 2 * i + 1
# parent of i = i // 2, (// integer divsion, rounds down)

class MinHeap:
    def __init__(self):
        self.minHeap = [0]

    def push(self, val):
        self.minHeap.append(val)
        i = len(self.minHeap) - 1

        # Percolate up as long as parent is larger than current.
        while i > 1 and self.minHeap[i] < self.minHeap[ i // 2]:
            temp = self.minHeap[i]
            self.minHeap[i] = self.minHeap[i // 2]

            self.minHeap[i // 2] = temp

            i = i // 2

    def pop(self):
        if len(self.minHeap) == 1:
            return None
        if len(self.minHeap) == 2:
            return self.minHeap.pop()

        result = self.minHeap[1]
        # Make the root node same value as the last node.
        self.minHeap[1] = self.minHeap.pop()

        # Take this value and percolate down as needed.
        self.percolate_down(1)

        return result


    def top(self):
        if len(self.minHeap) > 1:
            return self.minHeap[1]
        return None

    def heapify(self, nums):
        # Insert the dummy value in the beginning
        self.minHeap = [0] + nums

        # We start from the bottom to check if each node needs to be percolated down.
        # In a complete binary tree, 1/2 of the nodes are leaves, so half of the array already satisfies the heap properties.

        curr = (len(self.minHeap) - 1) // 2

        while curr > 0:
            self.percolate_down(curr)
            curr -= 1


    def percolate_down(self, i):
        # While left child exists.
        while 2 * i < len(self.minHeap):
            if (2 * i + 1 < len(self.minHeap) # If right child exists.
                and self.minHeap[2 * i + 1] < self.minHeap[2 * i] # If right child is smaller than the left child.
                and self.minHeap[2 * i + 1] < self.minHeap[i]): # If right child is smaller than the current node.

                # Swap current node with right child.
                temp = self.minHeap[i]
                self.minHeap[i] = self.minHeap[2 * i + 1]
                self.minHeap[2 * i + 1] = temp

                i = 2 * i + 1

            elif self.minHeap[2 * i] < self.minHeap[i]: # If left child is smaller than the current node.
                # Swap current node with left child.
                temp = self.minHeap[i]
                self.minHeap[i] = self.minHeap[2 * i]
                self.minHeap[2 * i] = temp

                i = 2 * i
            else:
                break


