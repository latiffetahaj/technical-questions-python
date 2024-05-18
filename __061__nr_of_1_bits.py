'''
    191. Number of 1 Bits
    Write a function that takes the binary representation of a positive integer and
    returns the number of set bits it has (also known as the Hamming weight).


    Constraints:
        1 <= n <= 2^31 - 1


    #LeetCode: https://leetcode.com/problems/number-of-1-bits/

    Time Complexity:
    Space Complexity:
'''

def hamming_weight(n):
    count = 0

    while n > 0:
        if (n & 1) == 1:
            count += 1

        n = n >> 1

    return count
