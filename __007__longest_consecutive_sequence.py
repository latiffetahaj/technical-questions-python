'''
    128. Longest Consecutive Sequence

    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    Constraints:
    You must write an algorithm that runs in O(n) time.

    #LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/description/

    Time Complexity: O(n)

    Space Complexity: O(n)
'''

def longest_sequence(nums):
    if nums is None or not nums:
        return 0

    max_seq = 0
    hash_set = set(nums) #populate the hashmap

    for nr in nums:
        if nr - 1 not in hash_set:
            current_seq = 0
            current = nr

            while current in hash_set:
                current_seq += 1
                current += 1

            if current_seq > max_seq:
                max_seq = current_seq

    return max_seq