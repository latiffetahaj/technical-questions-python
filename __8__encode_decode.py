'''
    String Encode Decode

    Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

    Please implement encode and decode

    #LeetCode: https://leetcode.com/problems/encode-and-decode-strings/description/

    Time Complexity: O(n) where n is the total number of characters in the list of strings.
                    If the input list has m strings, each with length t, then n = m * t

    Space Complexity: O(n)
'''

def encode(input):
    encoded = []
    for s in input:
        length = str(len(s))
        encoded.append(length)
        encoded.append('#')
        encoded.append(s)


    return ''.join(encoded)


def decode(str):
    result = []

    i = 0
    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1

        length = int(str[i:j])
        result.append(str[j + 1: j + 1 + length])
        i = j + 1 + length


    return result

