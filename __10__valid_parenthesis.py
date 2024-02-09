'''
    20. Valid Parentheses
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

    Constraints:
        1 <= s.length <= 10^4
        s consists of parentheses only '()[]{}'.

    Time Complexity: O(n)
    Space Complexity: O(n)

'''

def has_valid_parenthesis(input):
    stack = []
    pair = {'(':')', '[': ']', '{': '}'}

    for c in input:
        if c in pair:
            stack.append(c)
        elif not stack or pair[stack.pop()] != c:
            return False

    return not stack