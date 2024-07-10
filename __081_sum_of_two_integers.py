'''
    371. Sum of Two Integers
    Given two integers a and b, return the sum of the two integers without using the operators + and -.

    Constraints:
        -1000 <= a, b <= 1000

    #LeetCode: https://leetcode.com/problems/sum-of-two-integers/

    Time Complexity: O(32) at most we process only 32 bits inside a loop. => O(1)

    Space Complexity: O(1), not extra space is used to store the result.
'''
# In python integers are not bounded by a fixed length of bits, ex. int 32 or int 64.
# To avoid an infinite loop and incorrect results, given the constraints, we create a mask to filter only the first 32 bits.
# The mask is initialized as an hexadecimal number, but its bit representation is just 32 1-bits.


def sum_two_integers(a, b):
    mask = 0xffffffff

    while (mask & b) > 0:
        # Carry is going to be whenever there two bits 1, so whenever a & b = 1 at that particular bit.
        carry = a & b
        # XOR operator is useful here because:
        # 0 ^ 0 = 0, just like 0 + 0 = 0.
        # 0 ^ 1 = 1, just like 0 + 1 = 1.
        # 1 ^ 0 = 1, just like 1 + 0 = 1.
        # 1 ^ 1 = 0, just like 1 + 1 = 0. but one is carried on the bit to the left.

        a = a ^ b

        # Carry is shifted by one the left, and assigned it to b.
        b = carry << 1

# If b is not zer0, that means we have to filter the result and take only the first 32 bits.
    if b > 0:
        return (mask & a)
    else:
        # Otherwise we return the entire a, without filtering.
        return a