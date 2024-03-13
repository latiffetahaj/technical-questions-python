'''
    347. Top K Frequent Elements
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

    #LeetCode: https://leetcode.com/problems/top-k-frequent-elements/description/

    Time Complexity: O(n)

    Space Complexity: O(n)
'''

def top_k_elements(nums,k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    result = []


    #build the hashmap with frequencies
    for element in nums:
        count[element] = 1 + count.get(element,0)

    #build the result array, where the index shows the frequencies of those elements appeared
    #iterate through both key and values of the hashmap
    for key, value in count.items():
        freq[value].append(key)



    #build the result, loop from the end
    for i in range(len(freq) - 1, 0, -1):
        for element in freq[i]:
            result.append(element)

            if len(result) == k:
                return result

