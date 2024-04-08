'''
    46. Permutations
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    Constraints:
        1 <= nums.length <= 6
        -10 <= nums[i] <= 10
        All the integers of nums are unique.


    #LeetCode: https://leetcode.com/problems/permutations/description/

    Time Complexity: O(n!)
    Space Complexity: O(n!) will update later the exact space complexity
'''

#idea is to use a buffer (extra array of len(input)) to store current permutation
#also to use a boolean array that tells which items are currently in the buffer
#everytime the buffer is full, append to the result
def permutations(nums):

    input_length = len(nums)
    isInBuffer = [False] * input_length
    buffer = [0] * input_length
    permutations = []

    def generate_perm(bufferIndex):
        nonlocal input_length, permutations,nums,buffer,isInBuffer

        #when buffer is full
        if bufferIndex == input_length:
            #append a copy of the buffer to avoid passed by reference
            permutations.append(buffer.copy())
            return

        #find candiates to put in the buffer
        for i in range(input_length):
            #consider only the elements that currently are not in the buffer
            if not isInBuffer[i]:
                #place the element in the current buffer index
                buffer[bufferIndex] = nums[i]

                isInBuffer[i] = True
                #recursive call on the next index
                generate_perm(bufferIndex + 1)
                isInBuffer[i] = False

        return

    #function call
    generate_perm(0)

    return permutations