'''

    150. Evaluate Reverse Polish Notation
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation (post-fix).

    Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:
        The valid operators are '+', '-', '*', and '/'.
        Each operand may be an integer or another expression.
        The division between two integers always truncates toward zero.
        There will not be any division by zero.
        The input represents a valid arithmetic expression in a reverse polish notation.
        The answer and all the intermediate calculations can be represented in a 32-bit integer.

    Constraints:
        1 <= tokens.length <= 10^4
        tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

    #LeetCode: https://leetcode.com/problems/evaluate-reverse-polish-notation/

    Time Complexity: O(n)

    Space Complexity: O(n)
'''
import math
def evaluate_post_fix(tokens):

    stack = []

    for s in tokens:
        if s == '+' or s == '-' or s == '*' or s == '/':
            stack.append(calculate(stack.pop(),stack.pop(),s))
        else:
            stack.append(int(s))

    return stack.pop()


def calculate(second,first,op):
    if op == '+':
        return first + second
    elif op == '-':
        return first - second
    elif op == '*':
        return first * second
    else:
        #used math.trunc to truncate towards zero
        return math.trunc(first / second)