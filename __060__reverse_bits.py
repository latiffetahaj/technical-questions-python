'''
    190. Reverse Bits
    Reverse bits of a given 32 bits unsigned integer.


    Constraints:
        The input must be a binary string of length 32


    #LeetCode: https://leetcode.com/problems/reverse-bits/description/

    Time Complexity:  O(b) where b is the length of a given input in binary
    Space Complexity: O(1)
'''
# For testing purposes the function:
# Returns the string binary representation, with trailing zeros stripped.
# Also the input is given as a binary.
def reverse_bits(n):
    result = 0

    for i in range(32):
        extract_bit = (n >> i) & 1

        result = result | (extract_bit << (31 - i))


    return (bin(result)).rstrip('0')
