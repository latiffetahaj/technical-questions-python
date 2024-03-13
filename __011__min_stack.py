'''
    155. Min Stack
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:
        MinStack() - initializes the stack object.
        void push(int val) - pushes the element val onto the stack.
        void pop() - removes the element on the top of the stack.
        int top() - gets the top element of the stack.
        int getMin() - retrieves the minimum element in the stack.
        You must implement a solution with O(1) time complexity for each function.

    Constraints:
    -2^31 <= val <= 2^31 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.

    #LeetCode: https://leetcode.com/problems/min-stack/description/

    Time Complexity: O(1)

    Space Complexity: O(n)
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self,n):
        self.stack.append(n)
        if not self.min_stack or self.min_stack[-1] >= n:
            self.min_stack.append(n)

    def pop(self):
        #due to the constraints, no need to check if stack is empty
        current = self.stack.pop()
        if current == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
